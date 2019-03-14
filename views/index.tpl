<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="static/index.css">
    
    <title>Song Rank</title>
</head>

<body>
    <div class="container">
        
        <div class="row justify-content-around align-items-center">
            <div class="col-md-4">
                <div class="card song-card-a" data="{{song_pair[0].id}}">
                    % include('placeholder.tpl')
                    <div class="card-body">
                        <p class="card-text">{{song_pair[0].artist()}}</p>
                        <h5 class="card-title">{{song_pair[0].title()}}</h5>
                    </div>
                </div>
            </div>
            <div class="col-md-1">
                <h2>vs.</h2>
            </div>
            <div class="col-md-4">
                <div class="card song-card-b" data="{{song_pair[1].id}}">
                    % include('placeholder.tpl')
                    <div class="card-body">
                        <p class="card-text">{{song_pair[1].artist()}}</p>
                        <h5 class="card-title">{{song_pair[1].title()}}</h5>
                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-md-4">
            <div class="col-md-12">
                <p class="text-right"><b>{{str(num_counted)}}/{{str(size)}}</b></p>
            </div>
        </div>
        <div class="row mt-md-1">
            <div class="col-md-12">
                <ul class="list-group">
                    % [ include('song_list_view.tpl', index=x, song=song) for x, song in enumerate(song_list) ]
                </ul>
            </div>
        </div>
        
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.min.js" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="static/index.js"></script>
</body>

</html>
