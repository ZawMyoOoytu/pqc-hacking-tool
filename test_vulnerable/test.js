// vulnerable_crypto.js 
 
const crypto = require('crypto'); 
 
// ECDSA is quantum-vulnerable 
const { privateKey, publicKey } = crypto.generateKeyPairSync('ec', { 
  namedCurve: 'secp256k1' 
}); 
