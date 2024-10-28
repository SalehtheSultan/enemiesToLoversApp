// static/js/countdown.js

document.addEventListener('DOMContentLoaded', function() {
    var countDownDate = new Date("Nov 18, 2024 00:00:00").getTime();

    var countdownfunction = setInterval(function() {
        var now = new Date().getTime();
        var distance = countDownDate - now;

        if (distance < 0) {
            clearInterval(countdownfunction);
            document.getElementById("countdown").innerHTML = "Matches are now available!";
        } else {
            var days = Math.floor(distance / (1000 * 60 * 60 * 24));
            var hours = Math.floor(
                (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
            );
            var minutes = Math.floor(
                (distance % (1000 * 60 * 60)) / (1000 * 60)
            );
            var seconds = Math.floor(
                (distance % (1000 * 60)) / 1000
            );

            document.getElementById("countdown").innerHTML =
                days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
        }
    }, 1000);
});
