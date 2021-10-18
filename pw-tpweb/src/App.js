import logo from './logo.svg';
import './App.css';

function openNav() {
  document.getElementById("mobile__menu").style.width = "100%"
}
function closeNav() {
  document.getElementById("mobile__menu").style.width = "0"
}

function App() {
  return (
    <body>
  <div>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>

      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
  </div>
  </body>
  );
}

export default App;
