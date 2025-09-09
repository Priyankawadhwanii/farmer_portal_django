module.exports = {
  content: [
    "./templates/**/*.html",        // agar theme ke andar templates hain
    "../shop/templates/**/*.html",  // tumhara shop app ke templates
    "../templates/**/*.html",       // agar project level templates banoge
    "../**/*.py",                   // optional: agar classnames python files me likhe ho
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

