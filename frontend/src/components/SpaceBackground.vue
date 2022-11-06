<!--
<template>
  <div class="imageContainer">
    <a :id="imageLink" href="#"> <img :id="imageElement" /></a>
  </div>
</template>

<script>
export default {
  name: "SpaceBackground",
  data() {
    return {
      endpoint:
        "https://api.unsplash.com/photos/random/?client_id=SX8f-ypl054JtSFlkSmcP8PSTDZKbEKs79KxxvI6Dm4",
      imageElement: document.querySelector("#unsplashImage"),
      imageLink: document.querySelector("#imageLink"),
      creator: document.querySelector("#creator"),
    };
  },
  created() {
    fetch(this.endpoint)
      .then((response) => response.json())
      .then((jsonData) => {
        this.imageElement.src = jsonData.urls.regular;
        this.imageLink.setAttribute("href", jsonData.user.portfolio_url);
      })
      .catch((error) => {
        console.log("Error:" + error);
      });
  },
};
</script>

<style scoped></style>
-->
<template>
  <!--<div><img :src="image" class="img" /></div>-->
  <div class="hero"></div>
</template>

<script>
export default {
  name: "SpaceBackground",
  data() {
    return {
      acceskey: "SX8f-ypl054JtSFlkSmcP8PSTDZKbEKs79KxxvI6Dm4", // esta clave debe estar en el backend
      url: "https://api.unsplash.com/photos/random?query=scenery",
      image: "",
    };
  },
  methods: {
    fetchRandomPhoto() {
      fetch(this.url + `&client_id=${this.acceskey}`)
        .then((response) => response.json())
        .then((jsonData) => {
          this.image = jsonData.urls.raw + "&auto=format";
          console.log("jsonData", jsonData.urls.raw);
        })
        .catch((error) => console.log(error));
    },
  },
  created() {
    this.fetchRandomPhoto();
  },
};
</script>

<style scoped>
.hero {
  background-image: url("https://imgs.search.brave.com/impczdLryWnOTN4aRmZIbZIUpCjVJgDP3NLR2YP879M/rs:fit:1200:664:1/g:ce/aHR0cHM6Ly9lbG91/dHB1dC5jb20vYXBw/L3VwbG9hZHMtZWxv/dXRwdXQuY29tLzIw/MjAvMDYvVmFsb3Jh/bnQtbGFuemFtaWVu/dG8tb2ZpY2lhbC5q/cGc");
  background-attachment: fixed;
  position: relative;
  height: 100vh;
  display: flex;
}
.img {
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -100;
  background-size: cover !important;
  background-repeat: no-repeat !important;
}
</style>
