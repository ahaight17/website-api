module.exports = (app) => {

  const CORS = (req, res, next) => {
    res.header('Access-Control-Allow-Credentials', true)
    res.header('Access-Control-Allow-Origin', req.headers.origin)
    res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, DELETE, PUT')
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization, x-access-token, x-room-id')
    next()
  }

  app.get('/api', CORS, api)

  function api(req, res){
    res.status(200).send('YOU HEARD BACK FROM US')
  }

  return {}
}