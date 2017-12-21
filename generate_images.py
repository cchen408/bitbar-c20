#!/usr/bin/env python
from urllib import urlopen
import json
from PIL import Image
import StringIO
import base64

top_50_result = json.loads(urlopen('https://api.coinmarketcap.com/v1/ticker/?limit=50').read())


def process_image(token_image, symbol):
    print 'Processing {0}'.format(symbol)
    try:
        image = Image.open(StringIO.StringIO(token_image))
    except IOError:
        print "Could not identify image format for symbol '{0}', skipping...".format(symbol)
        return

    # Reduce image to 16x16
    resized_image = image.resize((16, 16), Image.ANTIALIAS)
    resized_image = image
    image_buffer = StringIO.StringIO()

    # Write image out with doubled DPI: 72->144
    resized_image.save(image_buffer, format=image.format, dpi=(144, 144))
    resized_image.save('token_images/{0}.png'.format(symbol), format=image.format, dpi=(144, 144))

    # Output 16x16 (144x144 dpi) base64 image for debugging
    print base64.b64encode(image_buffer.getvalue())


def main():
    for token in top_50_result:
        symbol = str(token['symbol']).lower()
        token_url = 'https://github.com/cjdowner/cryptocurrency-icons/blob/master/32/color/{0}.png?raw=true'.format(symbol)
        # The source is 32x32 token image
        token_image = urlopen(token_url).read()
        process_image(token_image, symbol)

if __name__ == '__main__':
    main()
