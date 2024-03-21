require 'shoes'

Shoes.app(title: "Loading Screen", width: 300, height: 150) do
  background "#FFF".."#EEE"
  @loading_label = para "Loading", align: "center"
  @dots = para "", align: "center"
  
  Thread.new do
    10.times do
      @dots.text += "."
      sleep(0.5)
    end
    @loading_label.text = "Loading Complete!"
  end
end
