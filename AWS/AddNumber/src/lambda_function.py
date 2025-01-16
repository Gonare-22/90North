import json

def lambda_handler(event, context):
    try:
        num1 = event.get('num1')
        num2 = event.get('num2')
        
        # Ensure the numbers are valid
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Both inputs must be numbers.")

        result = num1 + num2
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f"Missing parameter: {str(e)}"})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
