# Used Terms

## Story Terms

| Term            | Definition                                                                                       | Remarks |
| --------------- | ------------------------------------------------------------------------------------------------ | ------- |
| Alice           | Name of the person who takes the role of a citizen whose driving license is issued by DLAKa and who is a customer of BestRental | |
| AlicesAuthenticatorApp | An instance of Authenticator App used by Alice | |
| BestRental      | Name of the RC that offers cars for rent | |
| BestRentalApp   | Name of the microservice-based application to demonstrate the use of verifiable credentials in the context of car rental | |
| BestRentalPoC   | Name of the Proof of Concept (PoC) that demonstrates the concept of decentralized identities and verifiable credentials | |
| BestRentalVerifiableDataSystem | Name of the external system supporting BestRental with the realization of decentralized identity functionality (verification of VCs)| |
| Bob             | Name of the person who takes the role of a DLA Clerk working at DLAKa | |
| DLAKaApp        | Name of the microservice-based application the DLA uses to manage VC-DLs | |
| DLAKa           | Name of the DLA at Karlsruhe (Ka) that Bob works for and that is responsible for Alice's driving license  | |
| DLAKaVerifiableDataSystem | Name of the external system supporting the DLAKa with the realization of decentralized identity functionality (issuance/revocation of VCs) | |


## Business Terms
| Term            | Definition                                                                                       | Remarks |
| --------------- | ------------------------------------------------------------------------------------------------ | ------- |
| Authenticator App     | Multi-factor Authentication (MFA) app that also contains a VCWallet functionality. | |
| Citizen               | Role that is served by a DLA| |
| Customer              | Role that rents one or more cars from the car rental company | |
| Driving License Authority (DLA) | Department responsible for the management of driving licenses                                   |  |
| DLA Clerk             | Role that works in a DLA | |
| Rental Company (RC)   | Company that rents cars | |
| VC-DL                 | VC of a cititzen's driving license, representing a digital copy of a pyhsical driving license  | |
| Verfiable Data System | External system supporting the realization of decentralized identity functionality | |
| VP-DL                 | VP of a cititzen's driving license | |

## Architecture Terms
| Term              | Definition                                                                                       | Remarks |
| ------------------- | ------------------------------------------------------------------------------------------------ | ------- |
| BestRentalUI        | User interface of BestRentalApp. Used by Alice to rent a car. | |
| BestRentalTenant    | Azure tenant of BestRental. | |
| BestRentalWellKnown | A webserver serving the well-known path of the domain of BestRental, containing the DID document did.json. | |
| DLAKaUI             | User interface of DLAKaApp. Used by Bob to start VC-DL issuance requests. | |
| DLAKaTenant         | Azure tenant of DLAKa. | |
| DLAKaWellKnown      | A webserver serving the well-known path of the domain of DLAKa, containing the DID document did.json. | |
| DrivingLicenseManagement | Application microservice of DLAKaApp. Initiates VC-DL issuance requests to the Verifiable Data System.  | |
| RentalManagement    | Application microservice of BestRentalApp. Initiates VP-DLs to the Verifiable Data System.  | |



## Technical Terms

| Term            | Definition                                                                                       | Remarks |
| --------------- | ------------------------------------------------------------------------------------------------ | ------- |
| Decentralized Identifier (DID) | Globally unique persistent identifier that does not require a centralized registration authority and is often generated and/or registered cryptographically.| [W3C-Dec] |
| Verifiable Credential (VC) | Issuer-signed credential whose authenticity can be cryptographically verified. VCs are relevant to support decentralized identities. | [Ope-Ope] |
| Holder | Role an entity might perform by possessing one or more VCss and generating presentations from them. In this context Citizen-Alice performs this role. | [W3C-VCDM] |
| Issuer | Role an entity can perform by asserting claims about one or more subjects, creating a VC from these claims, and transmitting the VC to a holder.  In this context DLAApp performs this role. | [W3C-VCDM] |
| Verifier | Role an entity performs by receiving one or more VCs, optionally inside a verifiable presentation for processing. In this context BestRentalApp performs this role. | [W3C-VCDM] |
| Verifiable Presentation (VP) | Data derived from one or more VCs, issued by one or more issuers, that is shared with a specific verifier, e.g., presenting data from a  VC-DL. | [W3C-VCDM] |
| VCSchema | Blueprint for a VC. Enables an issuer to repeatedly issue VCs of the same kind. | [W3C-VCDM] |
| VCWallet | Can be used to store and present VCs by scanning QR-Codes from Issuers and Verrifiers. Coomunicates with the Verifiable Data Registry. | | |
| Verifiable Data Registry | The system is mediating the creation and verification of identifiers, keys, and other relevant data, such as verifiable credential schemas, revocation registries, issuer public keys, and so on, which might be required to use VCs | [W3C-VCDM] |
| OpenID Connect (OICD) | An authentication protocol that provides an identity layer on top of the OAuth 2.0 authorization framework, allowing for authentication of end-users against an authorization server. | |
| OAuth 2.0 | An open standard authorization protocol that provides a framework for allowing third-party applications to access user resources on a web service. | |

## Microsoft Entra Terms
| Term            | Definition                                                                                       | Remarks |
| --------------- | ------------------------------------------------------------------------------------------------ | ------- |
| Microsoft Entra |  Microsoft Entra is a comprehensive identity solution designed to simplify and streamline the process of managing digital identities. It provides robust tools and services that enable organizations to secure access, protect sensitive information, and maintain user privacy while offering a seamless user experience. Microsoft Entra includes amongst other products Azure Active Directory (Azure AD), Entra Verified ID, and the Microsoft Identity Platform. | |
| Microsoft Entra Verified ID | Decentralized identity platform built on Azure Active Directory (Azure AD) that allows scalable, secure, and privacy-preserving issuance and verification of VCs. | [MS-EVID] |
| Microsoft Identity Platform | Extends Azure AD by enabling developers to integrate authentication, single sign-on, and access control into their applications using industry-standard protocols such as OAuth 2.0 and OpenID Connect. It authorizes access to self-hosted applications and APIs registered in Azure AD or Microsoft APIs like the Verified ID Request API. The Microsoft Authentication Library (MSAL) allows seamless integration of the MicrosoftIdentityPlatform into any application. | [MS-IPD]|
| Azure Active Directory (Azure AD) | Cloud-based Identity and Access Management (IAM) service that provides a variety of features, such as single sign-on, multi-factor authentication, and device management. It allows organizations to manage and control access to their resources, applications, and data, ensuring security and compliance. | [MS-IPD] |
| Application Registration | The initial step in integrating an application with Azure AD. Upon completing the registration, a globally unique application object and a service principal object are automatically created within the home tenant. The Application Registration also provides essential information like the App ID, which uniquely identifies the application across the Azure ecosystem. Then secrets, certificates, permissions, and scopes can be configured to make the app work. | [MS-IPD] |
| Application Object | The application object in Azure AD is a blueprint residing in the application's home tenant, where it was registered. It serves as a template to create one or more service principal objects in every tenant where the application is utilized. Like a class in object-oriented programming, the application object has static properties that apply to all created service principal objects or application instances. The application object defines three aspects of an application: how the service can issue tokens for accessing the application, the resources the application might need, and the actions the application can perform. | [MS-IPD] |
| Service Principal | Created to facilitate secure access to resources within an Azure AD tenant. They act as an instance of the application and represent its identity in the tenant. Each service principal object is associated with a specific application object and inherits its permissions and settings. | [MS-IPD] |
| Contract | Microsoft Entra Verified ID specific term of VCSchema. Additonally contains a visual representation of the VC. | [MS-EVID]  |
| Verifiable Credentials Service | Internal Service responsible for executing the issuance of VCs. Since issuance requests are served by the VerifiableCredentialsRequestService, there has to be an interface between these two services. | [MS-EVID] |
| Verifiable Credentials Request Service | Provides the Request Service REST API. It serves issuance and presentation requests by interacting with the VerifiableCredentialService backend. Since it has Key/Sign permissions on the Azure key vault VerifiedIdVault it can sign messages using the stored key pairs. Relevant API specifications are the Request Service REST API issuance specification and Request Service REST API presentation specification. | [MS-EVID] |
| Verifiable Credentials Administration Service |  Provides the Verifiable credentials admin API, which allows the management of the Verifiable Credential service. It offers a way to set up a new authority, manage and create Verifiable Credential contracts and revoke Verifiable Credentials. It is accessed by the Azure Portal when configuring the service through the web UI. It further provides the Entra Verified ID network API, allowing the developer to search for published credentials in the Verified ID network. | [MS-EVID] |
| Azure Key Vault | Allows developers to securely store and manage cryptographic keys, certificates, and other secrets such as passwords, API keys, and connection strings. |  |
| VerifiedIDVault | Instance of Azure Key Vault storing the issuer and verifier keys, which are generated when a new Verified ID authority is set up. The keys and metadata are used to execute credential management operations and provide message security. Each verifier has a single key set used for signing, updating, and recovering VCs  | [MS-EVID] |



[Ope-Ope] OpenID Connect: OpenID for Verifiable Credential Issuance. https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html

[W3C-Dec] W3C: Decentralized Identifiers (DIDs) v1.0. https://www.w3.org/TR/did-core/

[W3C-VCDM] W3C: Verifiable Credentials Data Model v2.0 https://www.w3.org/TR/vc-data-model-2.0/

[MS-EVID] Microsoft: Microsoft Entra Verified ID documentation https://learn.microsoft.com/en-us/azure/active-directory/verifiable-credentials/

[MS-IPD] Microsoft: Microsoft identity platform documentation https://learn.microsoft.com/en-us/azure/active-directory/develop/