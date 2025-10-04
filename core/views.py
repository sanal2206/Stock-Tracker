from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import fetch_and_broadcast_stock

class SubmitStock(APIView):
    def post(self, request):
        symbols = request.data.get('symbols')  # expect a list of symbols
        if symbols and isinstance(symbols, list):
            for symbol in symbols:
                fetch_and_broadcast_stock.delay(symbol)
            
            return Response({"message": f"Stocks {', '.join(symbols)} submitted for tracking"})
        
        return Response({"error": "No symbols provided or invalid format"}, status=400)
