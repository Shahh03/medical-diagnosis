from flask import Blueprint, jsonify

from app.mongo.import_data import import_conditions
from app.page_collector.collect_nhs_pages import collect_all_pages


data_handling_api = Blueprint(
    "data_handling_api",
    __name__,
)


@data_handling_api.get("/health")
def data_health():
    return jsonify(
        {
            "success": True,
            "service": "data-handling-api",
            "status": "ok",
        }
    ), 200


@data_handling_api.post("/scrape/nhs")
def scrape_nhs():
    """
    Trigger NHS Inform A-Z scraping.

    The scraper is resumable because it loads the existing raw
    output file before collecting missing pages.
    """

    try:
        result = collect_all_pages()

        return jsonify(
            {
                "success": True,
                "message": "NHS scraping completed",
                "data": result,
            }
        ), 200

    except Exception as error:
        return jsonify(
            {
                "success": False,
                "message": "NHS scraping failed",
                "error": str(error),
            }
        ), 500


@data_handling_api.post("/import/conditions")
def import_condition_data():
    """
    Validate the conditioned five-field dataset and import/upsert
    it into MongoDB.
    """

    try:
        result = import_conditions()

        return jsonify(
            {
                "success": True,
                "message": "Condition dataset imported into MongoDB",
                "data": result,
            }
        ), 200

    except Exception as error:
        return jsonify(
            {
                "success": False,
                "message": "Condition import failed",
                "error": str(error),
            }
        ), 500
