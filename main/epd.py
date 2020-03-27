import framebuf
import epaper2in9b as epap
from machine import Pin, SPI, RTC
from Writer import Writer
import font10
import quote_api
import machine
import gc
gc.collect()

class DummyDisplay(framebuf.FrameBuffer):
    def __init__(self, buffer, width, height, format):
        self.height = height
        self.width = width
        self.buffer = buffer
        self.format = format
        super().__init__(buffer, width, height, format)

def epd_pull():
    #get the quote from the quote api function. Stored as tuple
    quote_list=quote_api.quote_pull()

    # software SPI on ESP32 Waveshare driver board
    sck = Pin(16)
    mosi = Pin(23)
    cs = Pin(5)
    busy = Pin(15)
    rst = Pin(21)
    dc = Pin(17)
    # miso is not used but must be declared. Let's take any unused gpio: 12
    miso = Pin(12)
    spi = SPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)

    e = epap.EPD(spi, cs, dc, rst, busy)
    e.init()

    h = 128;  w = 296 # e-paper heigth and width. It will be used in landscape mode

    buf_black        = bytearray(w * h // 8) # used by frame buffer (landscape)
    buf_red          = bytearray(w * h // 8) # used by frame buffer (landscape)
    buf_epaper_black = bytearray(w * h // 8) # used to display on e-paper after bytes have been 
    buf_epaper_red   = bytearray(w * h // 8) # moved from frame buffer to match e-paper (portrait) 

    fb_black = framebuf.FrameBuffer(buf_black, w, h, framebuf.MONO_VLSB)
    fb_red   = framebuf.FrameBuffer(buf_red,   w, h, framebuf.MONO_VLSB)
    black_red = 0 # will be black on buf_black, red on buf_red
    white     = 1

    d_b = DummyDisplay(buf_black, w, h, framebuf.MONO_VLSB)
    d_r = DummyDisplay(buf_red, w, h, framebuf.MONO_VLSB)
    d_b.fill(white)
    d_r.fill(white)

    wri_b = Writer(d_b, font10, False)
    Writer.set_textpos(d_b, 6, 0)  # verbose = False to suppress console output
    wri_b.printstring(quote_list[0], True)
    wri_r = Writer(d_r, font10, False)
    #import volt
    import hour_tim
    slep_tim=hour_tim.time_corr()
    #v_reading="%.2f" % volt.voltage()
    h='{:02d}:{:02d}.{:02d}'.format(RTC().datetime()[4],RTC().datetime()[5],RTC().datetime()[6])
    Writer.set_textpos(d_r, 110, 0) #y position 110 is max for font10
    print(h, quote_list[1])
    wri_r.printstring(' -'+quote_list[1]+' '+h, True)#+'  V='+v_reading

    # Move frame buffer bytes to e-paper buffer to match e-paper bytes organisation.
    x=0; y=0; n=1; R=0
    for i in range(1, 17):
        for j in range(1, 297):
            R = (n-x)+((n-y)*15)
            buf_epaper_black[R-1] = buf_black[n-1]
            buf_epaper_red[R-1] = buf_red[n-1]
            n +=1
        x = n+i-1
        y = n-1

    buf_red=[]
    buf_black=[]
    print('Sending to display')
    e.display_frame(buf_epaper_black, buf_epaper_red)
    print('Done!.......')
    gc.collect()
    e.sleep()  # recommended by manufacturer to avoid damage to display
    print('E-paper sleeping!...')
    machine.deepsleep(slep_tim)

    print('END')
