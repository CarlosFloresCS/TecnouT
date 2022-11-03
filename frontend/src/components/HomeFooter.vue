<template>
  <footer>
    <div class="footer-content">
      <h3>Tecnout</h3>
      <p>
        La aplicación busca crear un entorno de trabajo y socialización para
        estudiantes universitarios, buscando crear una comunidad mucho más
        organizada y colaborativa.
      </p>
      <ul class="socials">
        <li>
          <a href="#"
            ><img
              src="https://img.icons8.com/dusk/64/000000/facebook-new--v2.png"
          /></a>
        </li>
        <li>
          <a href="#"
            ><img src="https://img.icons8.com/cotton/64/000000/twitter.png"
          /></a>
        </li>
        <li>
          <a href="#"
            ><img src="https://img.icons8.com/dusk/64/000000/github.png"
          /></a>
        </li>
      </ul>
    </div>
    <div class="footer-bottom">
      <p>
        copyright &copy;2022 TecnouT. designed by <span>CarlosFlowers</span>
      </p>
    </div>
  </footer>
</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: #fcfcfc;
}

footer {
  background-color: rgba(22, 19, 28, 0.8);
  height: auto;
  width: auto;
  font-family: Open sans-serif;
  padding-top: 40px;
  color: #fff;
}

.footer-content {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center;
}

.footer-content h3 {
  font-size: 1.8rem;
  font-weight: 400;
  text-transform: capitalize;
  line-height: 3rem;
}

.footer-content p {
  max-width: 500px;
  margin: 10px auto;
  line-height: 28px;
  font-size: 14px;
}

.socials {
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 1rem 0 3rem 0;
}

.socials li {
  margin: 0 10px;
}

.socials a {
  text-decoration: none;
  color: #fff;
}

.socials a i {
  font-size: 1.1rem;
  transition: color 0.4s ease;
}

.socials a:hover i {
  color: aqua;
}

.footer-bottom {
  background: #000;
  width: auto;
  padding: 20px 0;
  text-align: center;
}

.footer-bottom p {
  font-size: 14px;
  word-spacing: 2px;
  text-transform: capitalize;
}

.footer-bottom span {
  text-transform: uppercase;
  opacity: 0.4;
  font-weight: 200;
}
</style>
