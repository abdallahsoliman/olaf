createStaff = ->
  $('<div class="rs-gradient" />').insertBefore $('.rs-tooltip')
  return

update = ->
  val = -230 + parseInt($('.rs-tooltip-text').html() * 7.5)
  $('.rs-gradient').css background: 'hsl(' + val + ', 100%, 57%)'
  return

val = 10 + Math.random() * 20
$('#slider').roundSlider
  radius: 80
  width: 15
  min: 10
  max: 100
  circleShape: 'pie'
  handleSize: '+16'
  handleShape: 'dot'
  sliderType: 'min-range'
  startAngle: 315
  value: val
  editableTooltip: false
  mouseScrollAction: true
  change: update
  drag: update
  create: ->
    createStaff()
    update()
    return
