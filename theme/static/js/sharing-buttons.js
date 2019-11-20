function initTwitterShare() {
  const twitterMessage = `${title} by Ricky White (@endlesstrax) #martialarts \n${link}`;
  const queryString = encodeURIComponent(twitterMessage); // Encodes the string to a URI querystring
  const twitterButton = document.getElementById("twitter-share");
  twitterButton.setAttribute("href", `https://twitter.com/intent/tweet?text=${queryString}`);
}

function initEmailShare() {
  const emailButton = document.getElementById("email-share");
  emailButton.setAttribute(
    "href",
    `mailto:?subject=${title}&body=I just read this article and thought you'd enjoy it, too.%0D%0A${link}`
  );
}

function initFacebookShare() {
  const facebookButton = document.getElementById("facebook-share");
  facebookButton.addEventListener("click", function() {
    console.log("clicked");
    FB.ui(
      {
        method: "share",
        href: `${link}`
      },
      function(response) {}
    );
  });
}

// Gets reuseable data - Post Title and the URL
const title = document.getElementById("article-title").innerHTML;
const link = window.location.href;

// Run all the things!
initTwitterShare();
initFacebookShare();
initEmailShare();