class GPSModule:
  vehicle_number = 'MH12AT9122'

  speed = [2.31,9.15,29.55,21.48,17.95,22.95,24.37,25.88,44.83,31.86,26.96,31.01,18.22,15.44,33.64,33.09,31.25,19.9,19.9,29.71,33.43,39.71,65.69,33.18,32.07,36.57,48.97,57.44,47.28,75.36,68.67,48.81,54.75,38.54,30.51,53.98,60.06,16.12,17.46,7.72,8.69,13.76,10.16,28.89,10.0,15.09,9.44,10.7,22.07, 25.43]
  
  # gps = [(18.508200,73.789722),(18.508199,73.789716),(18.508197,73.789740),(18.508213,73.789816),(18.508229,73.789870),(18.508234,73.789917),(18.508241,73.789977),(18.508260,73.790038),(18.508272,73.790105),(18.508293,73.790221),(18.508310,73.790303),(18.508326,73.790372),(18.508349,73.790450),(18.508349,73.790498),(18.508356,73.790538),(18.508366,73.790626),(18.508371,73.790713),(18.508364,73.790795),(18.508386,73.790842),(18.508366,73.790890),(18.508360,73.790968),(18.508347,73.791055),(18.508325,73.791157),(18.508321,73.791330),(18.508313,73.791417),(18.508298,73.791500),(18.508278,73.791594),(18.508276,73.791723),(18.508251,73.791872),(18.508240,73.791996),(18.508210,73.792192),(18.508193,73.792372),(18.508174,73.792499),(18.508150,73.792641),(18.508102,73.792729),(18.508116,73.792808),(18.508109,73.792950),(18.508084,73.793106),(18.508078,73.793148),(18.508078,73.793194),(18.508069,73.793212),(18.508075,73.793234),(18.508071,73.793270),(18.508058,73.793293),(18.508054,73.793369),(18.508058,73.793395),(18.508037,73.793428),(18.508048,73.793450),(18.508045,73.793478),(18.508041,73.793536)]
  gps = 18.479368, 73.807562

  index = -1

  def get_data(self):
      self.index += 1
      # return (self.gps[self.index % 50][0], self.gps[self.index % 50][1], self.speed[self.index % 50], vehicle_number)
      return (self.gps[0], self.gps[1], self.speed[self.index % 50], self.vehicle_number)
