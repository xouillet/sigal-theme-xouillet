#! /usr/bin/python

import datetime
import json


def date_reformat(value, format_to):
    return datetime.datetime.strptime(value, "%Y-%m-%d").strftime(format_to)


def panodata(media):
    pano_xmp = media.xmp["xmpmeta"]["RDF"]["Description"]
    if "UsePanoramaViewer" not in pano_xmp or pano_xmp["UsePanoramaViewer"] != "True":
        return "null"

    width_ratio = media.size["width"] / media.input_size["width"]
    height_ratio = media.size["height"] / media.input_size["height"]

    return json.dumps(
        {
            "fullWidth": int(pano_xmp["FullPanoWidthPixels"]) * width_ratio,
            "fullHeight": int(pano_xmp["FullPanoHeightPixels"]) * height_ratio,
            "croppedWidth": int(pano_xmp["CroppedAreaImageWidthPixels"]) * width_ratio,
            "croppedHeight": int(pano_xmp["CroppedAreaImageHeightPixels"])
            * height_ratio,
            "croppedX": int(pano_xmp["CroppedAreaLeftPixels"]) * width_ratio,
            "croppedY": int(pano_xmp["CroppedAreaTopPixels"]) * height_ratio,
        }
    )
