function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

fetch("passkey/begin_registration/")
  .then((response) => response.json())
  .then((data) => {
    const publicKey = {
      challenge: Uint8Array.from(window.atob(data.challenge), (c) =>
        c.charCodeAt(0)
      ),
      rp: {
        name: "Snowball",
        id: "0.0.0.0:8000",
      },
      user: {
        id: Uint8Array.from(window.atob(data.username), (c) => c.charCodeAt(0)),
        name: data.username,
        displayName: data.username,
      },
      pubKeyCredParams: [{ type: "public-key", alg: -7 }],
      authenticatorSelection: { authenticatorAttachment: "platform" },
    };

    return navigator.credentials.create({ publicKey });
  })
  .then((credential) => {
    const csrfToken = getCookie("csrftoken");

    console.log(credential);

    fetch("passkey/finish_registration/", {
      method: "POST",
      body: JSON.stringify(credential),
      headers: {
        "X-CSRFToken": csrfToken,
        "Content-Type": "application/json",
      },
    });
  });
