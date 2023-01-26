
var popularMovies = [];
var movies = [];

//displayMovies();


// genres = ["Action", "Comedy"]

async function getMovies() 
{
        url = "https://imdb-api.com/en/API/MostPopularMovies/k_1pvaf6m4";
        await $.ajax(url).done(async function (response) {
                movies = response;
        });
        console.log(movies)
}


async function getPopularMovies() 
{
        const settings = {
                "async": true,
                "crossDomain": true,
                "url": "https://most-popular-movies-right-now-daily-update.p.rapidapi.com/",
                "method": "GET",
                "headers": {
                        "X-RapidAPI-Key": "59acf3546cmsh0d1a19afef20499p135371jsn25d6436b4ae9",
                        "X-RapidAPI-Host": "most-popular-movies-right-now-daily-update.p.rapidapi.com"
                }
        };
        
        await $.ajax(settings).done(async function (response) {
                popularMovies = response;
        });

        // console.log(popularMovies);
}


async function displayMovies() 
{
        await getMovies();
       // popularMovies.forEach(element => {
                // for (let element = 0; element < movies.items.length; element++) {
    

                //         $(".feed-list").append(`
                // <div class="movie movie-box movie-main-box">
                //         <img class="movie-poster" src="${ movies.items[element].image}" alt="">
                //         <h3 class="movie-title">${movies.items[element].title}<p class="movie-year">${movies.items[element].year}</p></h3>
                // </div>`);   
                        
                // }
                
     //   });
}