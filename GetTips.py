import foursquare
import networkx as nx
#North Latitude: 40.915256 South Latitude: 40.491370 East Longitude: -73.700272 West Longitude: -74.259090
#See more at: http://www.mapdevelopers.com/geocode_bounding_box.php#sthash.A66HooOI.dpuf
G=nx.Graph()

G = nx.read_gml('graph.gml')
clat=nx.get_node_attributes(G, 'clat')
clong=nx.get_node_attributes(G, 'clong')
print clat
print clong

client = foursquare.Foursquare(access_token='NKAE2UBIMNTW2BLXKFXOFO50ZXPSTWYQHEXMCSWCLKSX0PCW')

for i in range(len(clat)):
    print i
    fo=open("tips_"+str(i), "a")
    print str(clat[i])+','+str(clong[i])
    exploreJson= client.venues.explore(params={'ll':str(clat[i])+','+str(clong[i]), 'radius':'500', 'limit':'100'})
    for j in range(len(exploreJson['groups'][0]['items'])):
        try:
            fo.write(exploreJson['groups'][0]['items'][j]['tips'][0]['text']+'\n')
        except:
            continue
    fo.close()
