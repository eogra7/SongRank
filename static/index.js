/* global $, jQuery */

$('.song-card-a').click(function() {
    var payload = {
        winner: $('.song-card-a').attr('data'),
        loser: $('.song-card-b').attr('data')
    };
    $.post('/evaluate', payload, function() {
        document.location.reload()
    });
});

$('.song-card-b').click(function() {
    var payload = {
        winner: $('.song-card-b').attr('data'),
        loser: $('.song-card-a').attr('data')
    };
    console.log(payload);
    jQuery.post('/evaluate', payload, function() {
        document.location.reload()
    });
});