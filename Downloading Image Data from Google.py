from simple_image_download import simple_image_download as sim

response = sim.simple_image_download

response().download('batmanjoker', 60)
response().download('thanosMarvel', 60)

#response().download('batmanjoker', 5,extensions={'.jpg'})
