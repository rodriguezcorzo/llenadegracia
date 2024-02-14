class Config:

    SECRET_KEY = '6547c09aad56961ec53cfaa155084e86'
    #! Deben ser desactivadas (FALSE)
    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/llenadegracia'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False #! Debe ser desactivada (FALSE)