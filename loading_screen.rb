require 'gosu'

class LoadingWindow < Gosu::Window
  def initialize
    super(200, 200, false)
    self.caption = "Loading"
    @background = Gosu::Image.new("loading.png")
    @start_time = Gosu.milliseconds
  end

  def update
    close if Gosu.milliseconds - @start_time >= 10000
  end

  def draw
    @background.draw(0, 0, 0)
  end
end

window = LoadingWindow.new
window.show
