'use strict';

class NavButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { selected: false };
  }

  render() {
    let classNames = this.state.selected ? "nav-button selected" : "nav-button" 

    return (
        <a href={this.props.link}>
            <button className="nav-button" onClick={() => this.setState({ selected: true }) }>
            {this.props.value}
            </button>
        </a>
    );
  }
}

class NavBar extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <NavButton 
                    link="/"
                    value="Home"
                />
                <NavButton
                    link="/hobbies"
                    value="Hobbies"
                />
                <NavButton
                    link="/map"
                    value="Map"
                />
                <NavButton
                    link="/timeline"
                    value="Timeline"
                />
            </div>
            
        )
    }
}

let domContainer = document.querySelector('#navbar_container');
let root = ReactDOM.createRoot(domContainer);
root.render(<NavBar />);