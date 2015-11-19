swampdragon.open ->
    # subscribe to heart rate channel
    swampdragon.subscribe 'heart-rate', 'heart-rate', null, ((context, data) ->
        return
    ), (context, data) ->
        return
    return

swampdragon.close ->
    return

swampdragon.ready ->
    return

swampdragon.onChannelMessage (channels, message) ->
    if channels[0] == "heart-rate" && message.action == "created"
        heartRateChart.push formatHeartRateData([message.data])
    return

formatHeartRateData = (heartRates) ->
    values = []
    for heartRate in heartRates
        values.push {time: new Date(heartRate.date).getTime()/1000, y: heartRate.value}
    return values

## Heart Rate Graph Preparation
heartRateChart = $('#heart-rate-graph').epoch
    type: 'time.line'
    data: [{
        label: 'Heart Rate'
        values: formatHeartRateData(data)
        range: [0, 100]
        ticks: { left: 10 }
    }]
    axes: ['bottom', 'left']
    ticks: { bottom: 10, left: 5}
    margins: { top: 25, right: 25, bottom: 25, left: 25 }
formatHeartRateData(data)
