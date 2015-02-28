<!DOCTYPE html>
<html>
  <head>
    <title>pi</title>
    <meta charset = "UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script type="text/javascript" src="{{ get_url('static', path='jquery/dist/jquery.min.js') }}" charset="utf-8"></script>
    <link rel="stylesheet" href="{{ get_url('static', path='bootstrap/dist/css/bootstrap.min.css') }}">
    <link rel="stylesheet" href="{{ get_url('original', path='original_style.css') }}">
  </head>
  <body>
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <p class="navbar-text">円周率10000桁にあなたが選んだ数字はあるかな？</p>
      </div>
    </nav>
    <div class="container">
      <div class="panel panel-success">
        <div class="panel-heading">
          <h3 class="panel-title">結果</h3>
        </div>
        <div class="panel-body">
          <p>{{search_result}}</p>
        </div>
      </div>
      <div class="panel panel-info">
        <div class="panel-heading">
          <h3 class="panel-title">合計得点</h3>
        </div>
        <div class="panel-body">
          <p>{{score_result}}点</p>
        </div>
      </div>
      <p><a href="/">もう一回やる</a></p>
    </div>
  </body>
</html>