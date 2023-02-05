
var popularMovies = [];
var movies = [];

//displayMovies();

// genres = ["Action", "Comedy"]

// const settings = {
// 	"async": true,
// 	"crossDomain": true,
// 	"url": "https://streaming-availability.p.rapidapi.com/get/basic?country=us&imdb_id=tt1375666&output_language=en",
// 	"method": "GET",
// 	"headers": {
// 		"X-RapidAPI-Key": "59acf3546cmsh0d1a19afef20499p135371jsn25d6436b4ae9",
// 		"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
// 	}
// };

// $.ajax(settings).done(function (response) {
// 	console.log(JSON.parse(response));
// });

// console.log("hi")

async function getMovies() 
{
        url = "https://imdb-api.com/en/API/MostPopularMovies/k_1pvaf6m4";
        await $.ajax(url).done(async function (response) {
                movies = response;
        });
}


async function displayMovies() 
{
        await getMovies();
        for (let element = 0; element < movies.items.length; element++) {
                $(".feed-list").append(`
                        <div class="movie movie-box movie-main-box">
                                <img class="movie-poster" src="${ movies.items[element].image}" alt="">
                                <h3 class="movie-title">${movies.items[element].fullTitle}</h3>
                        </div>`
                );   
                
        } 

        await $(".movie").click(function () {
                image = $(this).children(".movie-poster").attr("src");
                title = $(this).children(".movie-title").text();
        
                $(".side-bar-movie-box").children(".movie-poster").attr("src", image);
                $(".side-bar-movie-box").children(".movie-title").text(title);
        });
}

