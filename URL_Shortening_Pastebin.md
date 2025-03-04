## What is this System?
For example, if we shorten the following URL through ShorteningURL:

https://www.designsystems.org/course/grokking-the-system-design-interview

We would get:

https://shorteningurl.com/qxet23pt

## FR (Functional Requirements)
1. Shorten the URL (unique short identifier)
2. Redirect to Orginal URL
3. URL expiration (expiration timestamp)
4. User Account Management (Manage URLs, View Analytics - No. of clicks, location of user, referring platform)
5. Creating Custom Short URLs with specified keywords


## Non FR
1. Highly available (Short URLs must be accessible)
2. Security (Spamming, Phishing)
3. Scalability (Service must handle large number of users)
4. Performance (Fast retrieval (minimum latency when redirected to original URL))

## Cap Theorem
The CAP theorem says that a distributed system can deliver only two of three desired characteristics: **consistency, availability and partition tolerance** (the 'C,' 'A' and 'P' in CAP).

## PACELC Theorem
During a **network partition**, a distributed system must choose between **availability and consistency** 
When the system is running **normally**, it must choose between **latency and consistency** 

<img width="891" alt="image" src="https://github.com/user-attachments/assets/02475615-9d4e-44a3-a3ac-28a6934f8131" />

Multiple copies of data -> different servers -> how we sync b/w data? choose it. Most of the systems are supposed to be highly available during peak traffic and normally low latency -> making most customers happy and a few unhappy.

## Back-of-the-Envolope Estimations (Scale)
**Traffic Estimates**
- **New URL shortenings/sec** = 200 URLs/sec (518 million/month)
- **URL redirections/sec:** 100:1 read:write ratio.  20,000 URLs/sec

**Storage Estimates**
- **How many new URLs are stored**: 30 billion (518 * 12 * 5)
- **Storage**: Each URL may need 500 bytes (15TB) P.S.. TB has 12 zeros and PB 15 zeros more
- A petabyte is 1,000 terabytes (TB). A terabyte is 1,000 gigabytes (GB). A gigabyte is 1,000,000,000 bytes.

## System APIs
1. Create Short URL APIs
   Endpoint: POST/shorten
   Parameters:
     * original_url (string)
     * custom_alias (string)
     * expiration_date (timestamp/datetime)
     * user_id (string)
   Response:
    * shortened url (string), creation_date (timestamp), expiration_date (timestamp/datetime)
  
2. Redirect API
   Endpoint: GET/redirect
   Parameters:
   * shortened_url: (string)
   Response:
   * redirects to original_url
  
3. Analytics API
   Endpoint: GET/redirect
   Parameters:
   * shortened url: (string)
   * start_date (timestamp/datetime)
   * end_date (timestamp/datetime)
   Response:
   * click_count (integer)
   * unique_click (integer)
   * sites_referred_traffic_to_shortened_url (integer)
   * location_data (map)
   * device_data (map)

4. URL management API
   Endpoint: GET/ user/urls
   Parameters:
   * user_id: (string, required) (id of the user for whom urls are requested)
   * page (integer, optional) (for paginated results)
   * page_size (integer, optional) (for number of results per page)
   Response:
   * urls (list) : info like metadata like (creation_date, expiration_date)

6. Delete Shorten API
   Endpoint: DELETE /{shortened_url}
   Parameters:
   * shortened_url (string, required)
   * user_id (string, required)
   Response:
   * status (string)
  
## Database Schema (RDBMS / NoSQL)

**Table:**
* User: UserId (PK), Name, Email, PasswordHash, creation_date
* URL: Hash (PK), original_url, creation_date, expiration_date, UserId (FK)
* Analytics: AnalyticsId (PK), URLhash, click_timestamp, sites_referred_traffic_to_shortened_url, location

**Relationships:**
1 User ----> (can create) many -------> URLs
1 URL ----> (can create) many -------> Analytics

<img width="1397" alt="image" src="https://github.com/user-attachments/assets/7ad5b69e-47dc-4bf6-bf27-a2b2f907e033" />

### The image explains a basic system design and algorithm for generating a short and unique key for a given URL, typically used in URL shortening services.

#### Steps Involved:
Hashing & Encoding

The original URL (e.g., https://www.designgurus.org/course/grokking-the-system-design-interview) is taken as input.
A hash function such as MD5 or SHA256 is used to generate a 128-bit hash.
Example hash (MD5):
3c48c3223d7bbf0d5d0f02902eb0f305
Encoding the Hash

The hash is encoded using base36, base62, or base64 encoding to convert it into a shorter, URL-friendly string.
Example base64 encoding of the hash:
PEjDIj17vw1dDwKQLrDzBQ+P
Base64 uses characters A-Z, a-z, 0-9, +, / and results in around 21 characters.
Generating the Short Key

The first few characters of the encoded string are selected to form a short key.
Example short key:
PEjDIj (First 6 characters).
Issues:
Duplicate Short Keys for Identical URLs:
If two identical URLs are hashed, they will generate the same short key.
A solution is to append random salt or a unique identifier to ensure uniqueness.
Purpose:
This method is commonly used in URL shorteners like bit.ly or TinyURL, where long URLs are converted into short and manageable links.
Would you like more details on a specific part

## URL Redirection Workflow

<img width="1016" alt="image" src="https://github.com/user-attachments/assets/e21f79ca-ef9f-419d-adc2-4963ad23512e" />

## Cache

<img width="1307" alt="image" src="https://github.com/user-attachments/assets/0fe86013-91a0-4f5c-a81d-96cf57683547" />

Another possibility, App Server --->  Cache ---> DB

## Purging or DB cleanup

<img width="1278" alt="image" src="https://github.com/user-attachments/assets/59adf471-5d38-441f-9401-c09e0bace456" />

## System Design 1

<img width="1060" alt="image" src="https://github.com/user-attachments/assets/835f506b-43ab-4d6f-9270-dc21464b3ead" />

## Data Partitioning

<img width="1392" alt="image" src="https://github.com/user-attachments/assets/b94a441b-782d-4ad8-b61a-a15b088ee68f" />

<img width="1365" alt="image" src="https://github.com/user-attachments/assets/77767957-27c5-4806-9573-73f22b2d89af" />

## More

<img width="1316" alt="image" src="https://github.com/user-attachments/assets/3ef9e744-a099-48cd-b5a6-5d6b6caaa506" />

## FInal Diagram

<img width="768" alt="image" src="https://github.com/user-attachments/assets/c5af41be-5fe6-429e-9dcf-5b6a5854327e" />

<img width="862" alt="image" src="https://github.com/user-attachments/assets/8957cbe4-50d2-4ff7-b3be-e736acfaa5bd" />











   
