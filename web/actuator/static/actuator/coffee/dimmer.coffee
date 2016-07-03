class Dimmer

  raf: null
  mdown: false

  mPos:
    x: 0
    y: 0

  elementPosition:
    x: 0
    y: 0

  target: 0
  steps: 50
  radius: 150
  maxDiff: 150
  constraint: 360
  maxAngle: 250

  constructor: (@$context) ->
    @$body = $ ".dimmer-wrapper"
    @$knob = @$context.find ".knob"
    @$handle = @$context.find ".handle"
    @$progress = @$context.find ".progress"
    @$center = @$context.find ".center"
    @$textOutput = @$center.find "span"

    @ctx = @$progress.get(0).getContext "2d"

    knobOffset = @$knob.offset()

    @elementPosition =
      x: knobOffset.left
      y: knobOffset.top

    @centerX = @$progress.width()/2
    @centerY = @$progress.height()/2

    @canvasSize = @$progress.width()

    @addEventListeners()
    @drawLine()
    @draw()
    return


  addEventListeners: () ->
    @$context.on "mousedown", @onMouseDown
    @$context.on "mousemove", @onMouseMove
    $("body").on "mouseup", @onMouseUp
    return


  setDimmerPosition: ->
    @draw()
    return

  drawLine: (endAngle)->
    @ctx.save()

    @ctx.translate @centerX, @centerY
    @ctx.rotate (145*(Math.PI/180))
    startAngle = 0
    radius =  93
    x = 0
    y = 0
    @ctx.moveTo(98, 0)

    @ctx.beginPath()
    @ctx.shadowBlur = 10
    @ctx.lineWidth = 2.4
    @ctx.strokeStyle = "#fffdcf"
    @ctx.shadowBlur = 10
    @ctx.shadowColor = "#fff"
    @ctx.arc(x, y, radius, startAngle, endAngle, false)
    @ctx.stroke()


    @ctx.beginPath()
    @ctx.strokeStyle = "#7f7f7f"
    @ctx.shadowBlur = 0
    @ctx.arc(x, y, radius, endAngle, (@maxAngle*Math.PI)/180, false)
    @ctx.stroke()
    @ctx.restore()


  drawSteps: ->
    steps = 4
    @ctx.save()
    @ctx.translate @centerX, @centerY
    @ctx.rotate((135*Math.PI)/180)

    for i in [0..steps] by 1
      @ctx.beginPath()
      @ctx.rotate((180*Math.PI)/180 / steps)

      @ctx.strokeStyle = "#7f7f7f"
      @ctx.lineWidth = 2

      @ctx.lineTo(108, 0)
      @ctx.lineTo(100, 0)
      @ctx.stroke()

    @ctx.restore()
    return


  drawNumbers: () ->
    steps = 4
    angle = (180*(Math.PI/180))
    step = (180*Math.PI)/180 / steps
    radius = 116

    @ctx.translate @centerX, @centerY
    @ctx.save()

    for i in [0..steps] by 1
      x = (radius * Math.cos(angle))-4
      y = (radius * Math.sin(angle))+4
      angle += step

      @ctx.fillStyle = "#7f7f7f";
      @ctx.font = "bold 13px Arial";
      @ctx.fillText(i+1, x, y);

    @ctx.restore()


    @ctx.fillStyle = "#636262";
    @ctx.font = "normal 12px Arial";
    @ctx.fillText("OFF", -84, 75);
    @ctx.fillText("MAX", 62, 75);
    return


  draw: ()->
    @$progress.get(0).height = @canvasSize
    @$progress.get(0).width = @canvasSize

    endAngle = (@maxAngle*Math.PI)/180

    @drawLine((@target*Math.PI)/180)
    @drawSteps()
    @drawNumbers()
    @updateBackground()
    return


  updateBackground: ->
    normalizedTarget =  @map @target, 0, @maxAngle, 0, 1

    gray = parseInt(normalizedTarget*255,10)
    @$body.css
      #background: "#000 radial-gradient(230px at center, #8c8f95 0%, rgb(#{gray},#{gray},#{gray}) 100%) center center no-repeat"

    return

  setMousePosition: (event) ->
    @mPos =
      x: event.pageX - (@elementPosition.x + @centerX)
      y: event.pageY - (@elementPosition.y + @centerY)

    ang = Math.atan2 @mPos.x, @mPos.y
    if ang < 0 then ang = ang + 2 * Math.PI

    
    deg = 360 - (ang * (180/Math.PI))
    target = @map(deg, 0, 360, -40, 270)

    diff = Math.abs target - @target

    if diff < @maxDiff and target < @constraint
      @target = target

      if @target > @maxAngle then @target = @maxAngle
      if @target < 0 then @target = 0

    @setDimmerPosition()
    return


  # Callbacks
  onMouseDown: (event) =>
    @mdown = true
    return


  onMouseUp: (event) =>
    @mdown = false
    return


  onMouseMove: (event) =>
    if @mdown then @setMousePosition event
    return

  map: (value, low1, high1, low2, high2) ->
    return low2 + (high2 - low2) * (value - low1) / (high1 - low1)



@$dimmer = $ ".dimmer"
dimmer = new Dimmer @$dimmer
