from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def sqlite_chinook():    
    sqlite_engine = create_engine("sqlite:///sqlite/chinook.db")
    Base = declarative_base(sqlite_engine)
    class Tracks(Base):
    
        __tablename__ = 'tracks'
        __table_args__ = {'autoload':True}
    
    session = sessionmaker(bind=sqlite_engine)()    
    total_pages = session.query(Tracks).count()
    while True:
        
        print("Total Available pages: ", total_pages)
        page = int(input("Enter the page you want to access (-ve to exit):"))
        
        if page < 0:
            break
        elif page > total_pages:
            print('We don\'t have that much pages.')
            continue
        
        
        res = session.query(Tracks).order_by(Tracks.TrackId).offset(10*(page-1)).limit(10).all()                
        print("TrackId\t Track_name\t Composer\t Duration(mm:ss)")
        for track in res:            
            print(f"{track.TrackId}\t {track.Name}\t {track.Composer}\t {int((track.Milliseconds/60)/60)}:{int((track.Milliseconds/60)%60)}\t ")