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
          <h3 class="panel-title">現在の得点</h3>
        </div>
        <div class="panel-body">
          <p>{{score_result}}点</p>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-4"></div>
        <div class="col-lg-4">
          <form action="/second_result/" method="POST">
          <div class="input-group">
            <input type="number" class="form-control" placeholder="123456" name="second_number">
            <input type="hidden" name="total_score" value="{{score_result}}">
            <span class="input-group-btn">
              <button class="btn btn-default" type="submit">二回目</button>
            </span>
          </div><!-- /input-group -->
          </form>
        </div>
        <div class="col-lg-4"></div>
      </div><!-- /.row -->
    </div>
  </body>
</html>