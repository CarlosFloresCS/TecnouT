<template>
  <header>
    <nav>
      <div class="branding">
        <RouterLink to="/inicio"
          ><img
            class="logo"
            src="https://img.icons8.com/parakeet/48/000000/anubis.png"
        /></RouterLink>
      </div>
      <ul class="navigation">
        <li><router-link class="link" to="/">Home</router-link></li>
        <li><router-link class="link" to="/about">About</router-link></li>
        <li><router-link class="link" to="#">Contact</router-link></li>
      </ul>
      <div class="icon">
        <img src="https://img.icons8.com/cotton/35/000000/user.png" />
        <i class="far fa-bars"></i>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "HomeNavigation",
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap");
header {
  background-color: #16131ccc;
  z-index: 99;
  width: 100%;
  position: fixed;
  transition: 0.5s ease all;
  color: #fff;

  nav {
    display: flex;
    flex-direction: row;
    padding: 12px 0;
    transition: 0.5s ease all;
    width: 90%;
    margin: 0 auto;
    @media (min-width: 1140px) {
      max-width: 1140px;
    }

    ul,
    .link {
      font-weight: 500;
      color: #fff;
      list-style: none;
      text-decoration: none;
    }

    li {
      text-transform: uppercase;
      padding: 16px;
      margin-left: 16px;
      font-family: "Montserrat", sans-serif;
      font-weight: 500;
      font-size: 16px;
      color: #edf0f1;
      text-decoration: none;
    }

    .link {
      font-size: 14px;
      transition: 0.5s ease all;
      padding-bottom: 4px;
      border-bottom: 1px solid transparent;

      &:hover {
        color: #00afea;
        border: #00afea;
      }
    }

    .branding {
      display: flex;
      align-items: center;
      img {
        margin-left: -250px;
        width: 65px;
        transition: 0.5s ease all;
      }
    }

    .navigation {
      display: flex;
      align-items: center;
      flex: 1;
      justify-content: flex-end;
      padding: 15px 130px;
    }

    .icon {
      display: flex;
      align-items: center;
      position: absolute;
      top: 0;
      right: 24px;
      height: 100%;
      i {
        cursor: pointer;
        margin-left: 100px;
        font-size: 24px;
        transition: 0.8s ease all;
      }
    }
  }
}
</style>
