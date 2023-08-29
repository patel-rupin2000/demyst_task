def calculate_pre_assessment(application_data):
    # Apply rules to calculate preAssessment value
    print(application_data)
    profit_months = sum(1 for entry in application_data['profitOrLossSummary'] if entry['profitOrLoss'] > 0)
    average_asset_value = float(sum(entry['assetsValue'] for entry in application_data['profitOrLossSummary']) / len(
        application_data['profitOrLossSummary']))

    if profit_months > 0:
        pre_assessment = 60
    elif average_asset_value > float(application_data['loanAmount']):
        pre_assessment = 100
    else:
        pre_assessment = 20

    return pre_assessment


def submit_application(application_data):
    pre_assessment = calculate_pre_assessment(application_data)
    return {
        "applicationStatus": "Approved",
        "preAssessment": pre_assessment
    }
