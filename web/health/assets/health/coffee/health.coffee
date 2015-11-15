swampdragon.open ->
    # subscribe to heart rate channel
    swampdragon.subscribe 'heart-rate', 'heart-rate', null, ((context, data) ->
        console.log "subscribe success"
        return
    ), (context, data) ->
        console.log "subscribe fail"
        return
    return

swampdragon.close ->
    return

swampdragon.ready ->
    return

swampdragon.onChannelMessage (channels, message) ->
    console.log channels
    console.log message
    return

## Heart Rate Graph Preparation

margin =
    top: 25
    right: 25
    bottom: 25
    left: 25
width = 800 - margin.left - margin.right
height = 400 - margin.top - margin.bottom

# define scales and axes
xScale = d3.time.scale().range [0, width]
yScale = d3.scale.linear().range [height, 0]
xAxis = d3.svg.axis().scale(xScale).orient('bottom').ticks(10)
yAxis = d3.svg.axis().scale(yScale).orient('left').ticks(5)

# define the line
valueLine = d3.svg.line().x((d) ->
    xScale new Date(d.date)
).y((d) ->
    yScale d.value
)

# add svg canvas
svg = d3.select('#heart-rate-graph').append('svg').attr('width', width + margin.left + margin.right).attr('height', height + margin.top + margin.bottom).append('g').attr('transform', "translate(#{margin.left},#{margin.top})")

parseDate = d3.time.format("%d-%b-%y").parse

xScale.domain d3.extent(data, (d) ->
    new Date(d.date)
)
yScale.domain [
    d3.min(data, (d) ->
        d.value
    )
    d3.max(data, (d) ->
        d.value
    )
]

svg.append('path').attr('class', 'line').attr 'd', valueLine(data)
svg.append('g').attr('class', 'x axis').attr('transform', "translate(0, #{height})").call xAxis
svg.append('g').attr('class', 'y axis').call yAxis
