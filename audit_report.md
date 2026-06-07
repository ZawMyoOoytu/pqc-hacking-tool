# PQC Security Audit - Financial Sector 
 
## Target: teal-finance/quid 
    Algorithm: RSA
    Algorithm: RSA
    Context: // or the public key for asymmetric algos (like RSA, EdDSA).
    Algorithm: RSA
    Context: case "RS256", "RS384", "RS512": // RSA
    Algorithm: RSA
    Context: case "PS256", "PS384", "PS512": // RSA + salt
    Algorithm: RSA
    Context: // RSA: 2048 bits to prevent the error "message too long for RSA public key size"
    Algorithm: RSA
    Context: // RSA: 2048 bits to prevent the error "message too long for RSA public key size"
    Algorithm: RSA
    Context: // RSA + salt
    Algorithm: RSA
    Context: // GenerateKeyRSA generates a random RSA private key in DER format.
    Algorithm: RSA
    Algorithm: RSA
    Algorithm: ECDSA
    Algorithm: ECDSA
    Context: // - ES256 = ECDSA using P-256 and SHA-256
    Algorithm: ECDSA
    Context: // - ES384 = ECDSA using P-384 and SHA-384
    Algorithm: ECDSA
    Context: // - ES512 = ECDSA using P-521 and SHA-512
    Algorithm: ECDSA
    Context: // GenerateKeyECDSA generates a random ECDSA private key in DER format.
    Algorithm: ECDSA
    Algorithm: ECDSA
    Algorithm: Ed25519
    Algorithm: Ed25519
    Algorithm: Ed25519
    Algorithm: Ed25519
    Context: // - EdDSA = Ed25519
    Algorithm: Ed25519
    Algorithm: ECDSA
    Context: name:       "ES256=ECDSA-P256-SHA256",
    Algorithm: ECDSA
    Context: name:       "ES384=ECDSA-P384-SHA384",
    Algorithm: ECDSA
    Context: name:       "ES512=ECDSA-P521-SHA512",
    Algorithm: Ed25519
    Context: name:       "EdDSA=Ed25519",
    Algorithm: ECDSA
    Algorithm: ECDSA
    Context: type ECDSA struct {
    Algorithm: ECDSA
    Algorithm: ECDSA
    Context: ES256 struct{ ECDSA }
    Algorithm: ECDSA
    Context: ES384 struct{ ECDSA }
    Algorithm: ECDSA
    Context: ES512 struct{ ECDSA }
    Algorithm: ECDSA
    Context: ErrES256PubKey  = errors.New("cannot decode the ECDSA-P256-SHA256 public key, please provide 182 hex
    Algorithm: ECDSA
    Context: ErrES384PubKey  = errors.New("cannot decode the ECDSA-P384-SHA384 public key, please provide 240 hex
    Algorithm: ECDSA
    Context: ErrES512PubKey  = errors.New("cannot decode the ECDSA-P512-SHA512 public key, please provide 316 hex
    Algorithm: ECDSA
    Context: ErrECDSAPubKey  = errors.New("cannot parse the DER bytes as a valid ECDSA public key")
    Algorithm: ECDSA
    Algorithm: ECDSA
    Context: return &ES256{ECDSA{Base{reuse}, ecPubKey}}, nil
    Algorithm: ECDSA
    Algorithm: ECDSA
    Context: return &ES384{ECDSA{Base{reuse}, ecPubKey}}, nil
    Algorithm: ECDSA
    Algorithm: ECDSA
    Context: return &ES512{ECDSA{Base{reuse}, ecPubKey}}, nil
    Algorithm: ECDSA
    Context: func (v *ECDSA) verify(digest hash.Hash, headerPayload, sig []byte) bool {
    Algorithm: ECDSA
    Algorithm: ECDSA
    Context: func (v *ECDSA) verifySlower(digest hash.Hash, headerPayload, sig []byte) bool {
    Algorithm: ECDSA
    Algorithm: Ed25519
    Algorithm: Ed25519
    Algorithm: Ed25519
    Algorithm: RSA
    Context: - RS256 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-256
    Algorithm: RSA
    Context: - RS384 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-384
    Algorithm: RSA
    Context: - RS512 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-512
    Algorithm: ECDSA
    Context: - ES256 = ECDSA using P-256 and SHA-256
    Algorithm: ECDSA
    Context: - ES384 = ECDSA using P-384 and SHA-384
    Algorithm: ECDSA
    Context: - ES512 = ECDSA using P-521 and SHA-512
    Algorithm: Ed25519
    Context: - EdDSA = Ed25519
    Algorithm: RSA
    Context: - RS256 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-256
    Algorithm: RSA
    Context: - RS384 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-384
    Algorithm: RSA
    Context: - RS512 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-512
    Algorithm: ECDSA
    Context: - ES256 = ECDSA using P-256 and SHA-256
    Algorithm: ECDSA
    Context: - ES384 = ECDSA using P-384 and SHA-384
    Algorithm: ECDSA
    Context: - ES512 = ECDSA using P-521 and SHA-512
    Algorithm: Ed25519
    Context: - EdDSA = Ed25519
    Algorithm: RSA
    Context: - RS256 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-256
    Algorithm: RSA
    Context: - RS384 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-384
    Algorithm: RSA
    Context: - RS512 = RSASSA-PKCS1-v1_5 using 2048-bits RSA key and SHA-512
    Algorithm: ECDSA
    Context: - ES256 = ECDSA using P-256 and SHA-256
    Algorithm: ECDSA
    Context: - ES384 = ECDSA using P-384 and SHA-384
    Algorithm: ECDSA
    Context: - ES512 = ECDSA using P-521 and SHA-512
    Algorithm: Ed25519
    Context: - EdDSA = Ed25519
