document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("mediaModal");
    const modalImage = document.getElementById("modalImage");
    const modalVideo = document.getElementById("modalVideo");
    const videoSource = document.getElementById("videoSource");
    const closeButton = document.querySelector(".close");

    document.querySelectorAll(".clickable-media").forEach((media) => {
        media.addEventListener("click", (e) => {
            e.preventDefault();
            const mediaUrl = media.getAttribute("data-url");
            const mediaType = media.getAttribute("data-type");

            // Show the modal
            modal.style.display = "block";

            if (mediaType === "photo") {
                modalVideo.style.display = "none";
                modalImage.style.display = "block";
                modalImage.src = mediaUrl;
            } else if (mediaType === "video") {
                modalImage.style.display = "none";
                modalVideo.style.display = "block";
                videoSource.src = mediaUrl;
                modalVideo.load();
            }
        });
    });

    closeButton.addEventListener("click", () => {
        modal.style.display = "none";
        modalVideo.pause(); // Stop video playback
    });

    modal.addEventListener("click", (e) => {
        if (e.target === modal) {
            modal.style.display = "none";
            modalVideo.pause(); // Stop video playback
        }
    });
});
