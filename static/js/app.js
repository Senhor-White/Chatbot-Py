const introVideo = document.getElementById("intro-video");
const videoIntro = document.getElementById("video-intro");
const fallbackButton = document.getElementById("intro-fallback");
const introStatus = document.getElementById("intro-status");
const redirectUrl = videoIntro.dataset.redirectUrl;
const introDuration = 2;
let redirected = false;
let playbackFrame;

function redirectToMain() {
    if (redirected) {
        return;
    }

    redirected = true;
    cancelAnimationFrame(playbackFrame);
    introVideo.pause();
    window.location.replace(redirectUrl);
}

function finishAtLimit() {
    if (introVideo.currentTime < introDuration) {
        return false;
    }

    introVideo.currentTime = introDuration;
    redirectToMain();
    return true;
}

function monitorPlayback() {
    if (finishAtLimit()) {
        return;
    }

    playbackFrame = requestAnimationFrame(monitorPlayback);
}

function showPlaybackFallback(message, buttonLabel) {
    introStatus.textContent = message;
    fallbackButton.textContent = buttonLabel;
    fallbackButton.hidden = false;
}

function startPlayback() {
    introVideo.muted = true;
    introVideo.playsInline = true;

    const playback = introVideo.play();
    if (playback) {
        playback.then(() => {
            fallbackButton.hidden = true;
            playbackFrame = requestAnimationFrame(monitorPlayback);
        }).catch((error) => {
            console.error("Não foi possível iniciar o vídeo automaticamente.", error);
            if (introVideo.error) {
                return;
            }

            showPlaybackFallback(
                "A reprodução automática foi bloqueada.",
                "Iniciar vídeo"
            );
        });
    }
}

introVideo.loop = false;
introVideo.addEventListener("timeupdate", finishAtLimit);
introVideo.addEventListener("ended", redirectToMain);
introVideo.addEventListener("error", () => {
    console.error("Não foi possível carregar o vídeo da introdução.", introVideo.error);
    showPlaybackFallback(
        "Não foi possível carregar o vídeo da introdução.",
        "Continuar sem vídeo"
    );
});
fallbackButton.addEventListener("click", () => {
    if (introVideo.error) {
        redirectToMain();
        return;
    }

    startPlayback();
});

startPlayback();
