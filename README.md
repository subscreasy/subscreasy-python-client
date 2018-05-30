# swagger-client
Api Documentation

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = swagger_client.AnalyticsResourceApi()

try:
    # getDashboardAnalytics
    api_response = api_instance.get_dashboard_analytics_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsResourceApi->get_dashboard_analytics_using_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:8080*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnalyticsResourceApi* | [**get_dashboard_analytics_using_get**](docs/AnalyticsResourceApi.md#get_dashboard_analytics_using_get) | **GET** /api/analytics/dashboard | getDashboardAnalytics
*CardResourceApi* | [**create_card_using_post**](docs/CardResourceApi.md#create_card_using_post) | **POST** /api/cards | createCard
*CardResourceApi* | [**delete_card_using_delete**](docs/CardResourceApi.md#delete_card_using_delete) | **DELETE** /api/cards/{id} | deleteCard
*CardResourceApi* | [**get_all_cards_using_get**](docs/CardResourceApi.md#get_all_cards_using_get) | **GET** /api/cards | getAllCards
*CardResourceApi* | [**get_card_using_get**](docs/CardResourceApi.md#get_card_using_get) | **GET** /api/cards/{id} | getCard
*CardResourceApi* | [**update_card_using_put**](docs/CardResourceApi.md#update_card_using_put) | **PUT** /api/cards | updateCard
*ChargingLogResourceApi* | [**create_charging_log_using_post**](docs/ChargingLogResourceApi.md#create_charging_log_using_post) | **POST** /api/charging-logs | createChargingLog
*ChargingLogResourceApi* | [**delete_charging_log_using_delete**](docs/ChargingLogResourceApi.md#delete_charging_log_using_delete) | **DELETE** /api/charging-logs/{id} | deleteChargingLog
*ChargingLogResourceApi* | [**get_all_charging_logs_using_get**](docs/ChargingLogResourceApi.md#get_all_charging_logs_using_get) | **GET** /api/charging-logs | getAllChargingLogs
*ChargingLogResourceApi* | [**get_charging_log_using_get**](docs/ChargingLogResourceApi.md#get_charging_log_using_get) | **GET** /api/charging-logs/{id} | getChargingLog
*ChargingLogResourceApi* | [**refund_using_post**](docs/ChargingLogResourceApi.md#refund_using_post) | **POST** /api/charging-logs/refund/{chargingLogId} | refund
*ChargingLogResourceApi* | [**update_charging_log_using_put**](docs/ChargingLogResourceApi.md#update_charging_log_using_put) | **PUT** /api/charging-logs | updateChargingLog
*CompanyPropsResourceApi* | [**create_company_props_using_post**](docs/CompanyPropsResourceApi.md#create_company_props_using_post) | **POST** /api/company-props | createCompanyProps
*CompanyPropsResourceApi* | [**delete_company_props_using_delete**](docs/CompanyPropsResourceApi.md#delete_company_props_using_delete) | **DELETE** /api/company-props/{id} | deleteCompanyProps
*CompanyPropsResourceApi* | [**get_all_company_props_using_get**](docs/CompanyPropsResourceApi.md#get_all_company_props_using_get) | **GET** /api/company-props | getAllCompanyProps
*CompanyPropsResourceApi* | [**get_company_props_by_company_id_using_get**](docs/CompanyPropsResourceApi.md#get_company_props_by_company_id_using_get) | **GET** /api/company-props/company/{companyId} | getCompanyPropsByCompanyId
*CompanyPropsResourceApi* | [**update_company_props_using_put**](docs/CompanyPropsResourceApi.md#update_company_props_using_put) | **PUT** /api/company-props | updateCompanyProps
*CompanyResourceApi* | [**create_company_using_post**](docs/CompanyResourceApi.md#create_company_using_post) | **POST** /api/companies | createCompany
*CompanyResourceApi* | [**delete_company_using_delete**](docs/CompanyResourceApi.md#delete_company_using_delete) | **DELETE** /api/companies/{id} | deleteCompany
*CompanyResourceApi* | [**get_all_companies_using_get**](docs/CompanyResourceApi.md#get_all_companies_using_get) | **GET** /api/companies | getAllCompanies
*CompanyResourceApi* | [**get_company_using_get**](docs/CompanyResourceApi.md#get_company_using_get) | **GET** /api/companies/{id} | getCompany
*CompanyResourceApi* | [**update_company_using_put**](docs/CompanyResourceApi.md#update_company_using_put) | **PUT** /api/companies | updateCompany
*CouponResourceApi* | [**create_coupon_using_post**](docs/CouponResourceApi.md#create_coupon_using_post) | **POST** /api/coupons | createCoupon
*CouponResourceApi* | [**delete_coupon_using_delete**](docs/CouponResourceApi.md#delete_coupon_using_delete) | **DELETE** /api/coupons/{id} | deleteCoupon
*CouponResourceApi* | [**get_all_coupons_using_get**](docs/CouponResourceApi.md#get_all_coupons_using_get) | **GET** /api/coupons | getAllCoupons
*CouponResourceApi* | [**get_coupon_using_get**](docs/CouponResourceApi.md#get_coupon_using_get) | **GET** /api/coupons/{id} | getCoupon
*CouponResourceApi* | [**update_coupon_using_put**](docs/CouponResourceApi.md#update_coupon_using_put) | **PUT** /api/coupons | updateCoupon
*EndpointsApi* | [**authorize_using_put**](docs/EndpointsApi.md#authorize_using_put) | **PUT** /api/authorize | authorize
*EndpointsApi* | [**deduct_using_put**](docs/EndpointsApi.md#deduct_using_put) | **PUT** /api/deduct | deduct
*EndpointsApi* | [**get_authorized_services_using_get**](docs/EndpointsApi.md#get_authorized_services_using_get) | **GET** /api/service/subscriber/{secureId} | getAuthorizedServices
*EndpointsApi* | [**get_charging_log_by_subscription_using_get**](docs/EndpointsApi.md#get_charging_log_by_subscription_using_get) | **GET** /api/charging-logs/subscription/{id} | getChargingLogBySubscription
*EndpointsApi* | [**get_customer_total_amount_using_get**](docs/EndpointsApi.md#get_customer_total_amount_using_get) | **GET** /api/customer-totalAmountCharge/{id} | getCustomerTotalAmount
*EndpointsApi* | [**get_invoice_details_using_get**](docs/EndpointsApi.md#get_invoice_details_using_get) | **GET** /api/getInvoiceDetails | getInvoiceDetails
*EndpointsApi* | [**get_message_template_using_get**](docs/EndpointsApi.md#get_message_template_using_get) | **GET** /api/message-templates/email/{lifecycleEventName} | getMessageTemplate
*EndpointsApi* | [**get_service_instances_by_subscription_using_get**](docs/EndpointsApi.md#get_service_instances_by_subscription_using_get) | **GET** /api/service-instances/subscription/{id} | getServiceInstancesBySubscription
*EndpointsApi* | [**get_service_offerings_by_subscription_plan_using_get**](docs/EndpointsApi.md#get_service_offerings_by_subscription_plan_using_get) | **GET** /api/service-offerings/offer/{id} | getServiceOfferingsBySubscriptionPlan
*EndpointsApi* | [**get_total_revenue_per_month_using_get**](docs/EndpointsApi.md#get_total_revenue_per_month_using_get) | **GET** /api/charging-logs-totalamount-customer/{id} | getTotalRevenuePerMonth
*HistoryResourceApi* | [**create_history_using_post**](docs/HistoryResourceApi.md#create_history_using_post) | **POST** /api/histories | createHistory
*HistoryResourceApi* | [**delete_history_using_delete**](docs/HistoryResourceApi.md#delete_history_using_delete) | **DELETE** /api/histories/{id} | deleteHistory
*HistoryResourceApi* | [**get_all_histories_using_get**](docs/HistoryResourceApi.md#get_all_histories_using_get) | **GET** /api/histories | getAllHistories
*HistoryResourceApi* | [**get_history_using_get**](docs/HistoryResourceApi.md#get_history_using_get) | **GET** /api/histories/{id} | getHistory
*HistoryResourceApi* | [**update_history_using_put**](docs/HistoryResourceApi.md#update_history_using_put) | **PUT** /api/histories | updateHistory
*InvoiceResourceApi* | [**create_invoice_using_post**](docs/InvoiceResourceApi.md#create_invoice_using_post) | **POST** /api/invoices | createInvoice
*InvoiceResourceApi* | [**delete_invoice_using_delete**](docs/InvoiceResourceApi.md#delete_invoice_using_delete) | **DELETE** /api/invoices/{id} | deleteInvoice
*InvoiceResourceApi* | [**get_all_invoices_using_get**](docs/InvoiceResourceApi.md#get_all_invoices_using_get) | **GET** /api/invoices | getAllInvoices
*InvoiceResourceApi* | [**get_invoice_by_subscriber_using_get**](docs/InvoiceResourceApi.md#get_invoice_by_subscriber_using_get) | **GET** /api/invoices/subscriber/{subscriberSecureId} | getInvoiceBySubscriber
*InvoiceResourceApi* | [**get_invoice_using_get**](docs/InvoiceResourceApi.md#get_invoice_using_get) | **GET** /api/invoices/{id} | getInvoice
*InvoiceResourceApi* | [**update_invoice_using_put**](docs/InvoiceResourceApi.md#update_invoice_using_put) | **PUT** /api/invoices | updateInvoice
*MessageTemplateResourceApi* | [**create_message_template_using_post**](docs/MessageTemplateResourceApi.md#create_message_template_using_post) | **POST** /api/message-templates | createMessageTemplate
*MessageTemplateResourceApi* | [**delete_message_template_using_delete**](docs/MessageTemplateResourceApi.md#delete_message_template_using_delete) | **DELETE** /api/message-templates/{id} | deleteMessageTemplate
*MessageTemplateResourceApi* | [**get_all_message_templates_using_get**](docs/MessageTemplateResourceApi.md#get_all_message_templates_using_get) | **GET** /api/message-templates | getAllMessageTemplates
*MessageTemplateResourceApi* | [**get_message_template_using_get1**](docs/MessageTemplateResourceApi.md#get_message_template_using_get1) | **GET** /api/message-templates/{id} | getMessageTemplate
*MessageTemplateResourceApi* | [**update_message_template_using_put**](docs/MessageTemplateResourceApi.md#update_message_template_using_put) | **PUT** /api/message-templates | updateMessageTemplate
*OfferResourceApi* | [**create_offer_using_post**](docs/OfferResourceApi.md#create_offer_using_post) | **POST** /api/offers | createOffer
*OfferResourceApi* | [**delete_offer_using_delete**](docs/OfferResourceApi.md#delete_offer_using_delete) | **DELETE** /api/offers/{id} | deleteOffer
*OfferResourceApi* | [**get_all_offers_using_get**](docs/OfferResourceApi.md#get_all_offers_using_get) | **GET** /api/offers | getAllOffers
*OfferResourceApi* | [**get_offer_using_get**](docs/OfferResourceApi.md#get_offer_using_get) | **GET** /api/offers/{id} | getOffer
*OfferResourceApi* | [**update_offer_using_put**](docs/OfferResourceApi.md#update_offer_using_put) | **PUT** /api/offers | updateOffer
*ProfileInfoResourceApi* | [**get_active_profiles_using_get**](docs/ProfileInfoResourceApi.md#get_active_profiles_using_get) | **GET** /api/profile-info | getActiveProfiles
*ServiceInstanceResourceApi* | [**create_service_instance_using_post**](docs/ServiceInstanceResourceApi.md#create_service_instance_using_post) | **POST** /api/service-instances | createServiceInstance
*ServiceInstanceResourceApi* | [**delete_service_instance_using_delete**](docs/ServiceInstanceResourceApi.md#delete_service_instance_using_delete) | **DELETE** /api/service-instances/{id} | deleteServiceInstance
*ServiceInstanceResourceApi* | [**get_all_service_instances_using_get**](docs/ServiceInstanceResourceApi.md#get_all_service_instances_using_get) | **GET** /api/service-instances | getAllServiceInstances
*ServiceInstanceResourceApi* | [**get_service_instance_using_get**](docs/ServiceInstanceResourceApi.md#get_service_instance_using_get) | **GET** /api/service-instances/{id} | getServiceInstance
*ServiceInstanceResourceApi* | [**update_service_instance_using_put**](docs/ServiceInstanceResourceApi.md#update_service_instance_using_put) | **PUT** /api/service-instances | updateServiceInstance
*ServiceOfferingResourceApi* | [**create_service_offering_using_post**](docs/ServiceOfferingResourceApi.md#create_service_offering_using_post) | **POST** /api/service-offerings | createServiceOffering
*ServiceOfferingResourceApi* | [**delete_service_offering_using_delete**](docs/ServiceOfferingResourceApi.md#delete_service_offering_using_delete) | **DELETE** /api/service-offerings/{id} | deleteServiceOffering
*ServiceOfferingResourceApi* | [**get_all_service_offerings_using_get**](docs/ServiceOfferingResourceApi.md#get_all_service_offerings_using_get) | **GET** /api/service-offerings | getAllServiceOfferings
*ServiceOfferingResourceApi* | [**get_service_offering_using_get**](docs/ServiceOfferingResourceApi.md#get_service_offering_using_get) | **GET** /api/service-offerings/{id} | getServiceOffering
*ServiceOfferingResourceApi* | [**update_service_offering_using_put**](docs/ServiceOfferingResourceApi.md#update_service_offering_using_put) | **PUT** /api/service-offerings | updateServiceOffering
*ServiceResourceApi* | [**create_service_using_post**](docs/ServiceResourceApi.md#create_service_using_post) | **POST** /api/services | createService
*ServiceResourceApi* | [**delete_service_using_delete**](docs/ServiceResourceApi.md#delete_service_using_delete) | **DELETE** /api/services/{id} | deleteService
*ServiceResourceApi* | [**get_all_services_using_get**](docs/ServiceResourceApi.md#get_all_services_using_get) | **GET** /api/services | getAllServices
*ServiceResourceApi* | [**get_service_using_get**](docs/ServiceResourceApi.md#get_service_using_get) | **GET** /api/services/{id} | getService
*ServiceResourceApi* | [**update_service_using_put**](docs/ServiceResourceApi.md#update_service_using_put) | **PUT** /api/services | updateService
*SubscriberResourceApi* | [**create_subscriber_using_post**](docs/SubscriberResourceApi.md#create_subscriber_using_post) | **POST** /api/subscribers | createSubscriber
*SubscriberResourceApi* | [**delete_subscriber_using_delete**](docs/SubscriberResourceApi.md#delete_subscriber_using_delete) | **DELETE** /api/subscribers/{id} | deleteSubscriber
*SubscriberResourceApi* | [**get_all_subscribers_using_get**](docs/SubscriberResourceApi.md#get_all_subscribers_using_get) | **GET** /api/subscribers | getAllSubscribers
*SubscriberResourceApi* | [**get_subscriber_by_email_using_get**](docs/SubscriberResourceApi.md#get_subscriber_by_email_using_get) | **GET** /api/subscribers/email/{email} | getSubscriberByEmail
*SubscriberResourceApi* | [**get_subscriber_by_name_using_get**](docs/SubscriberResourceApi.md#get_subscriber_by_name_using_get) | **GET** /api/subscribers/name/{name} | getSubscriberByName
*SubscriberResourceApi* | [**get_subscriber_using_get**](docs/SubscriberResourceApi.md#get_subscriber_using_get) | **GET** /api/subscribers/{id} | getSubscriber
*SubscriberResourceApi* | [**update_subscriber_using_put**](docs/SubscriberResourceApi.md#update_subscriber_using_put) | **PUT** /api/subscribers | updateSubscriber
*SubsriptionResourceApi* | [**cancel_subscription_using_put**](docs/SubsriptionResourceApi.md#cancel_subscription_using_put) | **PUT** /api/subscriptions/cancel | cancelSubscription
*SubsriptionResourceApi* | [**get_active_subscriptions_using_get**](docs/SubsriptionResourceApi.md#get_active_subscriptions_using_get) | **GET** /api/subsriptions/subscriber/{secureId} | getActiveSubscriptions
*SubsriptionResourceApi* | [**get_all_company_subscriptions_using_get**](docs/SubsriptionResourceApi.md#get_all_company_subscriptions_using_get) | **GET** /api/subscriptions/company/{id} | getAllCompanySubscriptions
*SubsriptionResourceApi* | [**get_subsription_using_get**](docs/SubsriptionResourceApi.md#get_subsription_using_get) | **GET** /api/subsriptions/{id} | getSubsription
*SubsriptionResourceApi* | [**start_subscription_using_post**](docs/SubsriptionResourceApi.md#start_subscription_using_post) | **POST** /api/subscriptions/start | startSubscription
*UsageNotificationResourceApi* | [**create_usage_notification_using_post**](docs/UsageNotificationResourceApi.md#create_usage_notification_using_post) | **POST** /api/usage-notifications | createUsageNotification
*UsageNotificationResourceApi* | [**delete_usage_notification_using_delete**](docs/UsageNotificationResourceApi.md#delete_usage_notification_using_delete) | **DELETE** /api/usage-notifications/{id} | deleteUsageNotification
*UsageNotificationResourceApi* | [**get_all_usage_notifications_using_get**](docs/UsageNotificationResourceApi.md#get_all_usage_notifications_using_get) | **GET** /api/usage-notifications | getAllUsageNotifications
*UsageNotificationResourceApi* | [**get_usage_notification_using_get**](docs/UsageNotificationResourceApi.md#get_usage_notification_using_get) | **GET** /api/usage-notifications/{id} | getUsageNotification
*UsageNotificationResourceApi* | [**update_usage_notification_using_put**](docs/UsageNotificationResourceApi.md#update_usage_notification_using_put) | **PUT** /api/usage-notifications | updateUsageNotification
*UserResourceApi* | [**create_user_using_post**](docs/UserResourceApi.md#create_user_using_post) | **POST** /api/users | createUser
*UserResourceApi* | [**delete_user_using_delete**](docs/UserResourceApi.md#delete_user_using_delete) | **DELETE** /api/users/{login} | deleteUser
*UserResourceApi* | [**get_all_users_using_get**](docs/UserResourceApi.md#get_all_users_using_get) | **GET** /api/users | getAllUsers
*UserResourceApi* | [**get_authorities_using_get**](docs/UserResourceApi.md#get_authorities_using_get) | **GET** /api/users/authorities | getAuthorities
*UserResourceApi* | [**get_user_using_get**](docs/UserResourceApi.md#get_user_using_get) | **GET** /api/users/{login} | getUser
*UserResourceApi* | [**update_user_using_put**](docs/UserResourceApi.md#update_user_using_put) | **PUT** /api/users | updateUser


## Documentation For Models

 - [Address](docs/Address.md)
 - [Authority](docs/Authority.md)
 - [Authorization](docs/Authorization.md)
 - [AuthorizedServicesResponse](docs/AuthorizedServicesResponse.md)
 - [Cancellation](docs/Cancellation.md)
 - [ChargingLog](docs/ChargingLog.md)
 - [Company](docs/Company.md)
 - [CompanyProps](docs/CompanyProps.md)
 - [Coupon](docs/Coupon.md)
 - [Deduction](docs/Deduction.md)
 - [DeductionResult](docs/DeductionResult.md)
 - [History](docs/History.md)
 - [Invoice](docs/Invoice.md)
 - [InvoiceRequest](docs/InvoiceRequest.md)
 - [ManagedUserVM](docs/ManagedUserVM.md)
 - [MessageTemplate](docs/MessageTemplate.md)
 - [Offer](docs/Offer.md)
 - [PaymentCard](docs/PaymentCard.md)
 - [ProfileInfoVM](docs/ProfileInfoVM.md)
 - [RecurrencePeriod](docs/RecurrencePeriod.md)
 - [ResponseEntity](docs/ResponseEntity.md)
 - [SavedCard](docs/SavedCard.md)
 - [Service](docs/Service.md)
 - [ServiceInstance](docs/ServiceInstance.md)
 - [ServiceInstanceResult](docs/ServiceInstanceResult.md)
 - [ServiceOffering](docs/ServiceOffering.md)
 - [ServiceOfferingResult](docs/ServiceOfferingResult.md)
 - [StartSubscriptionRequest](docs/StartSubscriptionRequest.md)
 - [Subscriber](docs/Subscriber.md)
 - [SubscriptionCreateResult](docs/SubscriptionCreateResult.md)
 - [SubscriptionPlan](docs/SubscriptionPlan.md)
 - [Subsription](docs/Subsription.md)
 - [UsageNotification](docs/UsageNotification.md)
 - [User](docs/User.md)


## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



