function _all(q, e = document) { return e.querySelectorAll(q) }
function _one(q, e = document) { return e.querySelector(q) }


function toggleTweetModal() {
  _one("#tweetModal").classList.toggle("hidden")
}

async function signUp() {
  console.log("sign iup")
  const form = event.target
  // Get the button, set the data-await, and disable it
  const connection = await fetch("/signup", {
    method: "POST",
    body: new FormData(form)
  })

  if (!connection.ok) {
    return
  }

  connection_text = await connection.text();
  console.log(connection_text)
  if (connection_text == "valide") {
    window.location.href = "/login";
  }
  /** */

}

async function logIn() {
  console.log("iam login in");
  const form = event.target
  // Get the button, set the data-await, and disable it
  const connection = await fetch("/login", {
    method: "POST",
    body: new FormData(form)
  })

  if (!connection.ok) {
    return
  }


  connection_text = await connection.text();
  console.log(connection_text)
  window.location.href = connection_text;

}

async function delete_tweet(tweet_id) {
  //_one("#" + tweet_id).remove()
  //event.target.parentElement.parentElement.parentElement.parentElement.remove()
  //document.getElementById(tweet_id).remove()
  console.log(tweet_id)
  const connection = await fetch(`/delete/${tweet_id}`, {
    method: "DELETE",

  })
  if (!connection.ok) {
    return
  }

  document.querySelector(`[id='${tweet_id}']`).remove()





}

async function sendTweet() {
  const form = event.target
  // Get the button, set the data-await, and disable it
  const connection = await fetch("/create", {
    method: "POST",
    body: new FormData(form)
  })

  if (!connection.ok) {
    return
  }
  console.log(await connection);
  const connection_text = await connection.text();/* tweet id text*/
  const tweet_id = connection_text.slice(0, 36);
  const tweet_image = connection_text.slice(36, 40);
  const tweet_iat = connection_text.slice(40)
  console.log(connection_text, tweet_id, tweet_image, tweet_iat);

  const image_path = _one("input[type=file]", form).value.replaceAll(" ", "-").replaceAll("’", "").replaceAll("é", "e").replaceAll("(", "").replaceAll(")", "").trim()
  /*SUCCES*/
  let tweet = ''
  if (tweet_image == "true") {
    tweet = `
    <section
        class="tweet"
        id="${tweet_id}">
        <p class="Tweet_time">${tweet_iat}</p>
        <p class="mt-[2vw]">${_one("textarea", form).value}</p>
        <article >
          <button onclick="delete_tweet('${tweet_id}')">🗑️</button>
          <button onclick="openModuleUpdate('${tweet_id}','true' ,'${_one(" textarea", form).value}' , '/image/${image_path.substring(image_path.lastIndexOf("\\") + 1)}')">✏️</button>
        </article>
        <img src="/image/${image_path.substring(image_path.lastIndexOf("\\") + 1)}" alt="">
      </section>
    `
  } else {
    tweet = `
    <section class="tweet" id="${tweet_id}">
    <p class="Tweet_time">${tweet_iat}</p>
    <p class="mt-[2vw]">${_one("textarea", form).value}</p>
    <article >
      <button onclick="delete_tweet('${tweet_id}')">🗑️</button>
      <button onclick="openModuleUpdate('${tweet_id}','false' ,'${_one(" textarea", form).value}')">✏️</button>
    </article>
  </section>
    `
  }

  _one("#tweets").insertAdjacentHTML("afterbegin", tweet);


}

async function updateTweet() {
  const form = event.target
  // Get the button, set the data-await, and disable it
  const connection = await fetch("/update", {
    method: "PUT",
    body: new FormData(form)
  })

  if (!connection.ok) {
    return
  }
  const connection_text = await connection.text();/* tweet id text*/
  const connection_object = JSON.parse(connection_text);
  console.log(tweets);
  _one("#tweets").innerHTML = "";
  connection_object.tweets.forEach(tweet => {
    console.log(tweet.id);

    if (connection_object.user_id == tweet.user_id) {
      if (tweet.image) {
        const tweet_template = `
          <section class="tweet" id="${tweet.id}">
          <p class="Tweet_time">${tweet.iat}</p>
          <p>${tweet.description}</p>
          <article>
            <button onclick="delete_tweet('${tweet.id}')">🗑️</button>
            <button onclick="openModuleUpdate('${tweet.id}','true' ,'${tweet.description}' , '/image/${tweet.image}' )">✏️</button>
          </article>
          <img src="/image/${tweet.image}" alt="">
        </section>
      `
        _one("#tweets").insertAdjacentHTML("afterbegin", tweet_template);
        _one("#updating_module").style.display = " none";

      } else {
        const tweet_template = `
            <section class="tweet" id="${tweet.id}">
            <p class="Tweet_time">${tweet.iat}</p>
            <p>${tweet.description}</p>
            <article>
              <button onclick="delete_tweet('${tweet.id}')">🗑️</button>
              <button onclick="openModuleUpdate('${tweet.id}','false' ,'${tweet.description}')">✏️</button>
            </article>
          </section>
        `
        _one("#tweets").insertAdjacentHTML("afterbegin", tweet_template);
        _one("#updating_module").style.display = " none";



      }

    }

  });



}





function openModuleUpdate(tweet_id, is_image, tweet_text, image_path) {
  console.log(tweet_id, is_image, tweet_text, image_path)
  if (is_image === "true") {
    console.log("zs")
    _one("#updating_module #image_updating_div").style.display = "block";
    _one(" #image_updating_div img").setAttribute("src", image_path);
    _one("#image_updating_div").style.display = "flex";
    _one("#image_updating_div").style["align-items"] = "center";
    _one("#image_updating_div > input[type=checkbox]").checked = false;


  } else if (is_image === "false") {
    _one("#updating_module #image_updating_div").style.display = "none";

  }
  _one("#tweet_id_div input[type=text]").value = tweet_id;

  _one("#updating_module").style.display = "block";
  _one("#tweet_text_updator").value = tweet_text;
  console.log(tweet_text);
  document.getElementById("close_update").addEventListener("click", closeModuleUpdate);

}


function closeModuleUpdate() {
  _one("#updating_module").style.display = " none";

  console.log("yes");
}



