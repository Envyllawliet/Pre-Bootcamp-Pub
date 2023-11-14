console.log("page loaded...");

function over(element) {
    element.play();
}

function out(element) {
    element.pause();
}

function muteVideo() {
    var elemento_video = document.querySelector("#video");
    elemento_video.muted = !elemento_video.muted;
    elemento_video.play();
}