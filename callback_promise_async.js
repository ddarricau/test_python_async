
// Callback Hell
getData("/users/1", function (err, user) {
  if (err) {
    return;
  }
  getData(`${user.id}/posts`, function (err, posts) {
    if (err) {
      return;
    }
    getData(`${posts[0].id}/comments`, function (err, comments) {
      if (err) {
        return;
      }
      console.log(comments[0].body);
    });
  });
});

// Promises
getData("/users/1")
  .then(user => {
    return getData(`users/${user.id}/posts`);
  })
  .then(posts => {
    return getData(`/${posts[0].id}/comments`);
  })
  .then(comments => {
    console.log(comments[0].body);
  })
  .catch(err => console.error("Something went wrong:", err));

 // Async await
 try {
    const user = await getData("/users/1");
    const posts = await getData(`/users/${user.id}/posts`);
    const comments = await getData(`/${posts[0].id}/comments`);
    console.log(comments[0].body);

  } catch (error) {
    console.error("Something went wrong:", error);
  }
}