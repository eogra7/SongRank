<li class="list-group-item" {{song.elo if (song.elo != 1500) else 'hidden'}}>
    <div class="row align-self-center">
        <div class="col-md-11">
            <b>{{x + 1}}.</b> {{song.name}}
        </div>
        <div class="col-md-1">
            {{song.elo}}
        </div>
    </div>
</li>