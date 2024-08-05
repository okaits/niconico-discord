"use strict";
const video_id = window.location.pathname.split("/").pop();
const mutationObserver = new MutationObserver(() => {
    if (document.querySelectorAll('[data-name="video-content"]')[0]) {
        const player = document.querySelectorAll('[data-name="video-content"]')[0];
        const beacon_headers = {type: "application/json"}

        function start_video() {
            navigator.sendBeacon("http://localhost:36201/api/v1/start_watch", new Blob([JSON.stringify({video_id: video_id})], beacon_headers));
        };
        function seek_video() {
            navigator.sendBeacon("http://localhost:36201/api/v1/seek", new Blob([JSON.stringify({time: player.currentTime})], beacon_headers));
        };
        function stop_video() {
            navigator.sendBeacon("http://localhost:36201/api/v1/stop_watch");
        };

        player.addEventListener("play", start_video);
        player.addEventListener("pause", stop_video);
        player.addEventListener("waiting", stop_video);
        player.addEventListener("seeked", seek_video);
        player.addEventListener("ended", stop_video);
        window.addEventListener("unload", stop_video);

        mutationObserver.disconnect();
    };
});
mutationObserver.observe(document, {childList: true, subtree: true});
