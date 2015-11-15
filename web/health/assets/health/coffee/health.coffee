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

# prepare heart rate graph
margin =
    top: 25
    right: 25
    bottom: 25
    left: 25
width = 500 - margin.left - margin.right
height = 300 - margin.top - margin.bottom

