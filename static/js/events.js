
var gotStreaming = false;
var apiCallId = 0; /* use to make new api calls */

$(".frame").hide();
$(".streaming-logo").hide();

// $(".trailer-btn").click(function () {
//         $("body").addClass("background-tint");
//         $(".frame").show();
// })

// continue tut.

$(".close-stream").click(function () {
        gotStreaming = true;
        $(".watch-options").hide();
        $(".stream-btn").show();
});

$(".filter-items").click(function () {
        $(".active").removeClass("active");
        $(this).addClass("active");
})

$(".stream-btn").click(async function () {
        $(this).hide();
        $(".watch-options").css("display", "inline-block");
        id = $(".stream-id").val();

        if (!gotStreaming || (id != apiCallId)) { getStreaming(id); }
})

async function getStreaming(id) {
        apiCallId = id;
        const settings = {
                "async": true,
                "crossDomain": true,
                "url": "https://streaming-availability.p.rapidapi.com/get/basic?country=us&imdb_id=" + id + "&output_language=en",
                "method": "GET",
                "headers": {
                        "X-RapidAPI-Key": "59acf3546cmsh0d1a19afef20499p135371jsn25d6436b4ae9",
                        "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
                }
        };
        
        await $.ajax(settings).done(function (response) {
                gotStreaming = true;
                streaming = JSON.parse(response).streamingInfo;
                console.log(streaming);
                if (Object.keys(streaming).length != 0) {
                        platformsArr = Object.keys(streaming);
                        console.log(platformsArr);
                        platformsArr.forEach(platform => {
                                console.log(streaming[platform]);
                                $("." + platform).show();
                                $("." + platform).parents("a").attr("href", (streaming[platform]).us.link);
                        });
                } else {
                        $(".streaming-logo").hide();
                        $(".stream-option").append(`<p class="no-stream">This title is currently unavailable on all streaming services. Please check back soon.</p>`);
                }
        });
}