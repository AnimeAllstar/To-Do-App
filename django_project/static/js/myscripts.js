$('.star-wrapper').click(function (e) {
    e.preventDefault();
    var id;
    id = $(this).attr("data-id");
    $.ajax(
        {
            type: "GET",
            url: "/star",
            data: {
                item_id: id
            }
        })
});

$('.check-wrapper').click(function (e) {
    e.preventDefault();
    var id;
    id = $(this).attr("data-id");
    $.ajax(
        {
            type: "GET",
            url: "/check",
            data: {
                item_id: id
            }
        })
});

function toggleClass(star_btn) {
    if (star_btn.classList.contains("starred")) {
        star_btn.classList.remove("starred", "fas");
        star_btn.classList.add("unstarred", "far");
    } else if (star_btn.classList.contains("unstarred")) {
        star_btn.classList.remove("unstarred", "far");
        star_btn.classList.add("starred", "fas");
    }
}

function toggleClick(radio_btn) {
    if (radio_btn.classList.contains("fa-check-square")) {
        radio_btn.classList.remove("fa-check-square", "fas");
        radio_btn.classList.add("fa-square", "far");
    } else if (radio_btn.classList.contains("fa-square")) {
        radio_btn.classList.remove("fa-square", "far");
        radio_btn.classList.add("fa-check-square", "fas");
    }
}

window.addEventListener("pageshow", function (event) {
    var perfEntries = performance.getEntriesByType("navigation");

    if (perfEntries[0].type === "back_forward") {
        location.reload();
    }
});