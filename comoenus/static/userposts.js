var React = window.React
  , ReactDOM = window.ReactDOM;

var Post = React.createClass({
  render: function() {
    return (
      <div className="post">
        <h2 className="slim-title a-text demarginalize">
          <a href={"/post/"+this.props.slug+"_"+this.props.id_string}>
            {this.props.title}
          </a>
        </h2>
        <p className="demarginalize">
          <a href={"/user/"+this.props.username}>
            {this.props.username}
          </a> 
          {this.props.timestamp}
        </p>
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
      url: '/api/user_submissions_thumb',
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

ReactDOM.render(<PostList/>, document.getElementById('userposts'))
