var React = window.React
  , ReactDOM = window.ReactDOM;

var Post = React.createClass({
  handleVote: function(event) {
    var string = event.target.parentNode.parentNode.lastChild.firstChild.firstChild.href;
    var username = event.target.parentNode.parentNode.lastChild.lastChild.firstChild.innerHTML;
    var regexp = /_([a-z0-9]*)/g;
    var match = regexp.exec(string);
    var id_string = match[1];
    var eventClassName = event.target.classList[1];
    console.log(event.target);

    $.ajax({
      url: '/api/sub_vote:'+eventClassName+'/'+id_string+':'+username,
      type: 'POST',
    })
    .done(function(res) {
      console.log(res.status[0]+', value: '+res.status[1]);
      $( event.target ).toggleClass(eventClassName+'Mod');
      console.log(eventClassName+'Mod');
    })
    .fail(function() {
      console.log("error");
    })
    
  },
  render: function() {
    return (
      <div className="post">
        <div id="post-vote">
          <div id="vp" className="vote plus" onClick={this.handleVote}>
          </div>
          <div id="vm" className="vote minus" onClick={this.handleVote}>
          </div>
        </div>
        <div id="post-cont">
          <p className="title a-text demarginalize">
            <a href={"/post/"+this.props.slug+"_"+this.props.id_string}>
              {this.props.title}
            </a>
          </p>
          <p className="demarginalize">
            <a href={"/user/"+this.props.username}>
              {this.props.username}
            </a> 
            {this.props.timestamp}
          </p>
        </div>
      </div>
    )
  }
});

var PostList = React.createClass({
  getInitialState: function() {
    return {
      data: []
    }
  },
  loadPostsFromServer: function() {
    $.ajax({
      url: '/api/submissions_thumb',
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data.submissions});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(status, err.toString());
      }.bind(this)
    });
  },
  componentDidMount: function() {
    this.loadPostsFromServer();
    setInterval(this.loadPostsFromServer(), 1000)
  },
  render: function() {
    return (
      <div>
        {this.state.data.map(function(data) {
          return (
            <Post 
              key={data.id}
              slug={data.slug}
              id_string={data.id_string}
              title={data.title}
              username={data.user}
              timestamp={data.timestamp}
            />
          )
        })}
      </div>
    )
  }
});

ReactDOM.render(<PostList/>, document.getElementById('content-wrapper'))
