$('.star-wrapper, .check-wrapper').click(function (e) {
    e.preventDefault();
    var id = $(this).attr("data-id");
    var urlName = $(this).attr('class').replace(/-.*/, '');
    $.ajax(
        {
            type: "GET",
            url: "/" + urlName,
            data: {
                item_id: id
            }
        })
});

function toggleClass(star_btn) {
    if (star_btn.classList.contains("starred")) {
        star_btn.classList.remove("starred", "fas");
        star_btn.classList.add("unstarred", "far");
    } else {
        star_btn.classList.remove("unstarred", "far");
        star_btn.classList.add("starred", "fas");
    }
}

function toggleClick(radio_btn) {
    var item = document.getElementById(`i-${radio_btn.id}`);
    if (radio_btn.classList.contains("fa-check-square")) {
        radio_btn.classList.remove("fa-check-square", "fas");
        item.classList.remove("completed");
        radio_btn.classList.add("fa-square", "far");
    } else {
        radio_btn.classList.remove("fa-square", "far");
        radio_btn.classList.add("fa-check-square", "fas");
        item.classList.add("completed");
    }
}

window.addEventListener("pageshow", function (event) {
    var perfEntries = performance.getEntriesByType("navigation");

    if (perfEntries[0].type === "back_forward") {
        location.reload();
    }
});