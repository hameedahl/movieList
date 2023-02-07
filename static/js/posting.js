

$(".fa-star").click(function () {
        if ($(this).hasClass("fa-regular")) {
                $(this).removeClass("fa-regular");
                $(this).css("color", "#9142ff");
                $(this).addClass("fa-solid");
        } else {
                $(this).css("color", "#fff");
                $(this).addClass("fa-regular");
                $(this).removeClass("fa-solid");
        }
});



function queryMovie(title, title_type) {
        url = `https://imdb-api.com/API/AdvancedSearch/k_1pvaf6m4?title=${title}&title_type=${title_type}&languages=en`
        var settings = {
                "url": url,
                "method": "GET",
                "timeout": 0,
        };
               
        $.ajax(settings).done(function (response) {
                console.log(response);
        });
}
