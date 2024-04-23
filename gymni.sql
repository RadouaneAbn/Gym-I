--
-- PostgreSQL database dump
--

-- Dumped from database version 12.18 (Ubuntu 12.18-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.18 (Ubuntu 12.18-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: amenities; Type: TABLE; Schema: public; Owner: radouane
--

CREATE TABLE public.amenities (
    name character varying(128) NOT NULL,
    id character varying(60) NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.amenities OWNER TO radouane;

--
-- Name: cities; Type: TABLE; Schema: public; Owner: radouane
--

CREATE TABLE public.cities (
    name character varying(128) NOT NULL,
    id character varying(60) NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.cities OWNER TO radouane;

--
-- Name: clients; Type: TABLE; Schema: public; Owner: radouane
--

CREATE TABLE public.clients (
    first_name character varying(128) NOT NULL,
    last_name character varying(128) NOT NULL,
    email character varying(128) NOT NULL,
    password character varying(128) NOT NULL,
    id character varying(60) NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.clients OWNER TO radouane;

--
-- Name: gym_amenity; Type: TABLE; Schema: public; Owner: radouane
--

CREATE TABLE public.gym_amenity (
    gym_id character varying(60) NOT NULL,
    amenity_id character varying(60) NOT NULL
);


ALTER TABLE public.gym_amenity OWNER TO radouane;

--
-- Name: gymes; Type: TABLE; Schema: public; Owner: radouane
--

CREATE TABLE public.gymes (
    name character varying(128) NOT NULL,
    city_id character varying(60) NOT NULL,
    owner_id character varying(60) NOT NULL,
    location character varying(256) NOT NULL,
    description character varying(1024),
    price_by_month integer NOT NULL,
    price_by_year integer NOT NULL,
    profile_picture character varying(256),
    links character varying[],
    id character varying(60) NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.gymes OWNER TO radouane;

--
-- Name: owners; Type: TABLE; Schema: public; Owner: radouane
--

CREATE TABLE public.owners (
    first_name character varying(128) NOT NULL,
    last_name character varying(128) NOT NULL,
    email character varying(128) NOT NULL,
    password character varying(128) NOT NULL,
    id character varying(60) NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.owners OWNER TO radouane;

--
-- Name: reviews; Type: TABLE; Schema: public; Owner: radouane
--

CREATE TABLE public.reviews (
    gym_id character varying(60) NOT NULL,
    client_id character varying(60) NOT NULL,
    text character varying(1024) NOT NULL,
    id character varying(60) NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.reviews OWNER TO radouane;

--
-- Data for Name: amenities; Type: TABLE DATA; Schema: public; Owner: radouane
--

COPY public.amenities (name, id, created_at, updated_at) FROM stdin;
Security cameras	31ff1ce9-f0a5-4b60-9557-4b0b14b34730	2024-04-23 16:31:13.958557	2024-04-23 16:31:13.958678
Energy-efficient lighting and equipment	13c22a6b-75ef-449f-a855-66219eb82b72	2024-04-23 16:32:20.085257	2024-04-23 16:32:20.085353
First-aid stations	1a0956b0-a0fd-49a6-8088-4f83abeb3b60	2024-04-23 16:32:40.196415	2024-04-23 16:32:40.19651
Emergency exits and alarms	21797e6f-2c30-41ef-86b4-c11f52bedcb4	2024-04-23 16:32:53.704721	2024-04-23 16:32:53.704825
Parking lots	9300886c-bdb0-4971-8544-81b33435aad7	2024-04-23 16:33:05.378825	2024-04-23 16:33:05.37892
Bicycle racks	8e636ccc-a839-443f-b931-1f3f7af4f496	2024-04-23 16:33:11.821746	2024-04-23 16:33:11.821865
Accessible facilities for disabled members	466e82e0-93d4-4b33-b47d-47d2250108be	2024-04-23 16:33:26.421185	2024-04-23 16:33:26.421283
Wi-Fi	9f728cd0-6030-4d4c-8ac6-9d8e56e4e772	2024-04-23 16:33:36.151764	2024-04-23 16:33:36.151871
Music	edda47ff-513e-4b53-b137-11e057c9066a	2024-04-23 16:33:53.874392	2024-04-23 16:33:53.874497
TV screens for entertainment	1dbb85e9-e477-4278-989a-62151fee61ed	2024-04-23 16:34:07.938541	2024-04-23 16:34:07.938665
Lounges	92fde6f8-cc50-4708-bb5a-4397b98ac832	2024-04-23 16:34:18.3992	2024-04-23 16:34:18.399295
Cafeterias or snack bars	9283b594-5869-4303-a5b8-116eaea15a53	2024-04-23 16:34:26.322639	2024-04-23 16:34:26.322736
Retail shops	ecbb91fe-e75b-4f8f-a3e5-44c3124aa7b9	2024-04-23 16:34:42.974113	2024-04-23 16:34:42.974238
Kids' playrooms	2e6c65e7-60ea-4d26-bba2-0f60b369854b	2024-04-23 16:34:50.967038	2024-04-23 16:34:50.967132
Supervised childcare	3ef96ff9-7f14-4a2a-b633-e1761f4fe328	2024-04-23 16:34:57.825639	2024-04-23 16:34:57.825731
Showers	8567bb52-5658-422b-93fa-3f6efaa05b3a	2024-04-23 16:35:26.917463	2024-04-23 16:35:26.917572
Lockers	0713b69c-42d3-4ddc-a9b3-5a7aec6db0bd	2024-04-23 16:35:31.93126	2024-04-23 16:35:31.931352
Changing rooms	a4bf35ea-901a-40c3-bfed-d2f7e7acdc27	2024-04-23 16:35:38.367952	2024-04-23 16:35:38.36808
Toilets	b4660a5e-ed5a-47b9-901d-4a08da9cdf69	2024-04-23 16:35:44.101418	2024-04-23 16:35:44.101484
Nutrition consulting	55a2e4b0-8823-4429-9ff1-63bd026b0742	2024-04-23 16:36:05.443683	2024-04-23 16:36:05.443815
Personal training	d1543e47-c464-4b0f-80b5-65bb1df09dd6	2024-04-23 16:36:10.103258	2024-04-23 16:36:10.10332
Basketball courts	3f098c38-20ba-44da-813d-fddbc07da52a	2024-04-23 16:36:31.637781	2024-04-23 16:36:31.63788
Racquetball/squash courts	c51c258a-5dbf-47c4-8a38-9876f29a4577	2024-04-23 16:36:37.86585	2024-04-23 16:36:37.865962
Tennis courts	c483db6e-9c77-4a42-8d37-2c0bba7cddf2	2024-04-23 16:36:50.550298	2024-04-23 16:36:50.550401
Indoor soccer fields	07e08912-f883-4188-858e-281724ad4a9a	2024-04-23 16:36:56.826537	2024-04-23 16:36:56.826675
Swimming pools	d44d89d9-cea1-4c1b-a2fd-0e4563ce4123	2024-04-23 16:37:04.607619	2024-04-23 16:37:04.607715
Steam rooms	c2c5ea9a-305e-4591-8717-4c8d8eac34eb	2024-04-23 16:48:17.771279	2024-04-23 16:48:17.771406
fitness class rooms	951513c1-716d-44e9-a77d-fa5bb3f9db96	2024-04-23 16:48:38.523139	2024-04-23 16:48:38.523231
Yoga studios	8fc12192-32f7-4423-8e30-96b962e47524	2024-04-23 16:48:49.346576	2024-04-23 16:48:49.346679
Boxing area	cb894db6-2be5-47fc-a23b-6c54a8e316f8	2024-04-23 18:45:08.565815	2024-04-23 18:45:08.56591
\.


--
-- Data for Name: cities; Type: TABLE DATA; Schema: public; Owner: radouane
--

COPY public.cities (name, id, created_at, updated_at) FROM stdin;
Casablanca	c77d94e6-9f82-4db1-8298-e69c64554cd4	2024-04-23 17:29:25.724387	2024-04-23 17:29:25.724433
Rabat	f5ecd4d2-fc08-47b2-b46d-046ab96421cb	2024-04-23 17:29:25.737201	2024-04-23 17:29:25.737262
Fes	3b80074e-7de8-4f57-9436-f7b8ddf71895	2024-04-23 17:29:25.739709	2024-04-23 17:29:25.739748
Marrakech	0ff3e63b-be77-421d-b819-f0b6002d4bed	2024-04-23 17:29:25.741981	2024-04-23 17:29:25.742013
Tangier	c987eead-e7cc-4c83-80ac-6f5f525240d7	2024-04-23 17:29:25.744276	2024-04-23 17:29:25.744306
Agadir	1584bbaf-1207-4cff-94d9-ba6c0ca9d0c3	2024-04-23 17:29:25.746299	2024-04-23 17:29:25.746337
Meknes	d2ce0370-b5e7-42f3-84d2-ac0fc92d264a	2024-04-23 17:29:25.748407	2024-04-23 17:29:25.748448
Oujda	bde97455-8ab8-4449-82ad-5f17e603edbf	2024-04-23 17:29:25.750428	2024-04-23 17:29:25.750465
Kenitra	820989f0-79d6-4963-9345-358131df0ed5	2024-04-23 17:29:25.752276	2024-04-23 17:29:25.752307
Tetouan	cb0f1e0f-c0e2-4084-90ed-eff4cbd5ab00	2024-04-23 17:29:25.75419	2024-04-23 17:29:25.754221
Safi	1b776f43-3741-44d7-81be-29c5364c4365	2024-04-23 17:29:25.756098	2024-04-23 17:29:25.75614
Mohammedia	21ac7d9d-035d-46c4-9003-dd32155aa05c	2024-04-23 17:29:25.758731	2024-04-23 17:29:25.758793
Khouribga	795d1f5f-4997-4c63-b743-e8ebfa6802a8	2024-04-23 17:29:25.761395	2024-04-23 17:29:25.761449
Beni Mellal	308bb434-5493-4979-b04e-227833f64334	2024-04-23 17:29:25.764357	2024-04-23 17:29:25.764424
El Jadida	1eca88fd-f45f-4241-8878-863c5b265a62	2024-04-23 17:29:25.767164	2024-04-23 17:29:25.767227
Taza	d9c2844e-a2b0-4784-9761-ff170feb186f	2024-04-23 17:29:25.769845	2024-04-23 17:29:25.769912
Nador	eb1db4a5-452a-4bfb-9487-916c3653cce5	2024-04-23 17:29:25.773018	2024-04-23 17:29:25.773089
Settat	0909259a-2133-4c15-9e46-2f4b11395216	2024-04-23 17:29:25.775876	2024-04-23 17:29:25.775946
Larache	44961b9b-dc6d-406a-9e90-63037473de65	2024-04-23 17:29:25.778569	2024-04-23 17:29:25.778642
Ksar El Kebir	84598629-b6d2-4990-993e-e4ea0066fd4c	2024-04-23 17:29:25.781477	2024-04-23 17:29:25.781545
Essaouira	d1e80930-eb44-433c-a362-fc290a2c28a8	2024-04-23 17:29:25.784407	2024-04-23 17:29:25.784474
Taounate	42fbad70-f6f6-457a-9b77-e5fbe4940cb1	2024-04-23 17:29:25.787329	2024-04-23 17:29:25.787403
Sidi Kacem	fca416d6-760c-4e42-a2b1-0e649041c34e	2024-04-23 17:29:25.790117	2024-04-23 17:29:25.790188
Sidi Slimane	b1d2f4e7-0c0c-4252-8978-14c2cd6a0078	2024-04-23 17:29:25.793327	2024-04-23 17:29:25.793396
Chefchaouen	39700420-28a6-4578-9bf5-7c0f640565df	2024-04-23 17:29:25.79614	2024-04-23 17:29:25.796206
Azrou	ef7e51f0-f105-47ac-ab04-583d24452283	2024-04-23 17:29:25.799267	2024-04-23 17:29:25.79934
Al Hoceima	e556c5b8-88ec-4ce2-b5c8-6697b663c991	2024-04-23 17:29:25.801886	2024-04-23 17:29:25.801957
Errachidia	b3d6c735-d610-4823-a2d5-e4e37fc20353	2024-04-23 17:29:25.804908	2024-04-23 17:29:25.804986
Zagora	eece6808-7f39-4e7b-bcb2-db24ea249c0c	2024-04-23 17:29:25.808428	2024-04-23 17:29:25.80851
Ouarzazate	f17db0f1-41cc-4cb2-965f-5703020a40a0	2024-04-23 17:29:25.811289	2024-04-23 17:29:25.811355
\.


--
-- Data for Name: clients; Type: TABLE DATA; Schema: public; Owner: radouane
--

COPY public.clients (first_name, last_name, email, password, id, created_at, updated_at) FROM stdin;
Oumaima	NAANAA	oumaima@gmail.com	81dc9bdb52d04dc20036dbd8313ed055	389f660e-affa-4b4f-96f7-cebbff6a238a	2024-04-23 16:21:30.592361	2024-04-23 16:21:30.59245
Badr	ANNABI	badr@gmail.com	81dc9bdb52d04dc20036dbd8313ed055	8521800d-e9fa-480f-9ac3-23802720e1a8	2024-04-23 16:21:50.599437	2024-04-23 16:21:50.599486
Zidane	ZAOUI	zidane@gmail.com	81dc9bdb52d04dc20036dbd8313ed055	1650c20e-9eab-449c-9d3f-7fe441eef070	2024-04-23 16:22:14.798867	2024-04-23 16:22:14.798946
\.


--
-- Data for Name: gym_amenity; Type: TABLE DATA; Schema: public; Owner: radouane
--

COPY public.gym_amenity (gym_id, amenity_id) FROM stdin;
bd24d3d1-a644-4106-9ece-3d09089f2269	31ff1ce9-f0a5-4b60-9557-4b0b14b34730
bd24d3d1-a644-4106-9ece-3d09089f2269	13c22a6b-75ef-449f-a855-66219eb82b72
bd24d3d1-a644-4106-9ece-3d09089f2269	9300886c-bdb0-4971-8544-81b33435aad7
bd24d3d1-a644-4106-9ece-3d09089f2269	8e636ccc-a839-443f-b931-1f3f7af4f496
bd24d3d1-a644-4106-9ece-3d09089f2269	466e82e0-93d4-4b33-b47d-47d2250108be
bd24d3d1-a644-4106-9ece-3d09089f2269	9f728cd0-6030-4d4c-8ac6-9d8e56e4e772
bd24d3d1-a644-4106-9ece-3d09089f2269	edda47ff-513e-4b53-b137-11e057c9066a
bd24d3d1-a644-4106-9ece-3d09089f2269	1dbb85e9-e477-4278-989a-62151fee61ed
bd24d3d1-a644-4106-9ece-3d09089f2269	9283b594-5869-4303-a5b8-116eaea15a53
bd24d3d1-a644-4106-9ece-3d09089f2269	8567bb52-5658-422b-93fa-3f6efaa05b3a
bd24d3d1-a644-4106-9ece-3d09089f2269	0713b69c-42d3-4ddc-a9b3-5a7aec6db0bd
bd24d3d1-a644-4106-9ece-3d09089f2269	a4bf35ea-901a-40c3-bfed-d2f7e7acdc27
2493a598-c8ce-470d-a03a-cea3ad8fcff7	31ff1ce9-f0a5-4b60-9557-4b0b14b34730
2493a598-c8ce-470d-a03a-cea3ad8fcff7	13c22a6b-75ef-449f-a855-66219eb82b72
2493a598-c8ce-470d-a03a-cea3ad8fcff7	9300886c-bdb0-4971-8544-81b33435aad7
2493a598-c8ce-470d-a03a-cea3ad8fcff7	8e636ccc-a839-443f-b931-1f3f7af4f496
2493a598-c8ce-470d-a03a-cea3ad8fcff7	466e82e0-93d4-4b33-b47d-47d2250108be
2493a598-c8ce-470d-a03a-cea3ad8fcff7	9f728cd0-6030-4d4c-8ac6-9d8e56e4e772
2493a598-c8ce-470d-a03a-cea3ad8fcff7	1dbb85e9-e477-4278-989a-62151fee61ed
2493a598-c8ce-470d-a03a-cea3ad8fcff7	9283b594-5869-4303-a5b8-116eaea15a53
2493a598-c8ce-470d-a03a-cea3ad8fcff7	8567bb52-5658-422b-93fa-3f6efaa05b3a
2493a598-c8ce-470d-a03a-cea3ad8fcff7	0713b69c-42d3-4ddc-a9b3-5a7aec6db0bd
2493a598-c8ce-470d-a03a-cea3ad8fcff7	a4bf35ea-901a-40c3-bfed-d2f7e7acdc27
2493a598-c8ce-470d-a03a-cea3ad8fcff7	d44d89d9-cea1-4c1b-a2fd-0e4563ce4123
2493a598-c8ce-470d-a03a-cea3ad8fcff7	8fc12192-32f7-4423-8e30-96b962e47524
2493a598-c8ce-470d-a03a-cea3ad8fcff7	ecbb91fe-e75b-4f8f-a3e5-44c3124aa7b9
2493a598-c8ce-470d-a03a-cea3ad8fcff7	2e6c65e7-60ea-4d26-bba2-0f60b369854b
2493a598-c8ce-470d-a03a-cea3ad8fcff7	3ef96ff9-7f14-4a2a-b633-e1761f4fe328
f5ee9697-646c-49ff-8153-3a48ac7ee865	31ff1ce9-f0a5-4b60-9557-4b0b14b34730
f5ee9697-646c-49ff-8153-3a48ac7ee865	13c22a6b-75ef-449f-a855-66219eb82b72
f5ee9697-646c-49ff-8153-3a48ac7ee865	9300886c-bdb0-4971-8544-81b33435aad7
f5ee9697-646c-49ff-8153-3a48ac7ee865	8e636ccc-a839-443f-b931-1f3f7af4f496
f5ee9697-646c-49ff-8153-3a48ac7ee865	466e82e0-93d4-4b33-b47d-47d2250108be
f5ee9697-646c-49ff-8153-3a48ac7ee865	9f728cd0-6030-4d4c-8ac6-9d8e56e4e772
f5ee9697-646c-49ff-8153-3a48ac7ee865	8567bb52-5658-422b-93fa-3f6efaa05b3a
f5ee9697-646c-49ff-8153-3a48ac7ee865	0713b69c-42d3-4ddc-a9b3-5a7aec6db0bd
f5ee9697-646c-49ff-8153-3a48ac7ee865	a4bf35ea-901a-40c3-bfed-d2f7e7acdc27
f5ee9697-646c-49ff-8153-3a48ac7ee865	d44d89d9-cea1-4c1b-a2fd-0e4563ce4123
f5ee9697-646c-49ff-8153-3a48ac7ee865	8fc12192-32f7-4423-8e30-96b962e47524
f5ee9697-646c-49ff-8153-3a48ac7ee865	ecbb91fe-e75b-4f8f-a3e5-44c3124aa7b9
f5ee9697-646c-49ff-8153-3a48ac7ee865	2e6c65e7-60ea-4d26-bba2-0f60b369854b
f5ee9697-646c-49ff-8153-3a48ac7ee865	3ef96ff9-7f14-4a2a-b633-e1761f4fe328
f5ee9697-646c-49ff-8153-3a48ac7ee865	d1543e47-c464-4b0f-80b5-65bb1df09dd6
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	31ff1ce9-f0a5-4b60-9557-4b0b14b34730
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	13c22a6b-75ef-449f-a855-66219eb82b72
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	9300886c-bdb0-4971-8544-81b33435aad7
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	8e636ccc-a839-443f-b931-1f3f7af4f496
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	466e82e0-93d4-4b33-b47d-47d2250108be
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	9f728cd0-6030-4d4c-8ac6-9d8e56e4e772
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	8567bb52-5658-422b-93fa-3f6efaa05b3a
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	0713b69c-42d3-4ddc-a9b3-5a7aec6db0bd
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	a4bf35ea-901a-40c3-bfed-d2f7e7acdc27
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	d44d89d9-cea1-4c1b-a2fd-0e4563ce4123
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	8fc12192-32f7-4423-8e30-96b962e47524
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	ecbb91fe-e75b-4f8f-a3e5-44c3124aa7b9
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	2e6c65e7-60ea-4d26-bba2-0f60b369854b
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	3ef96ff9-7f14-4a2a-b633-e1761f4fe328
45cf2b21-a1b1-4831-8e37-4dbc553d2d26	d1543e47-c464-4b0f-80b5-65bb1df09dd6
bc53c1a8-b0af-4af0-9dc4-22f557f54d34	edda47ff-513e-4b53-b137-11e057c9066a
bc53c1a8-b0af-4af0-9dc4-22f557f54d34	8567bb52-5658-422b-93fa-3f6efaa05b3a
bc53c1a8-b0af-4af0-9dc4-22f557f54d34	0713b69c-42d3-4ddc-a9b3-5a7aec6db0bd
bc53c1a8-b0af-4af0-9dc4-22f557f54d34	a4bf35ea-901a-40c3-bfed-d2f7e7acdc27
bc53c1a8-b0af-4af0-9dc4-22f557f54d34	9300886c-bdb0-4971-8544-81b33435aad7
29248f0a-4203-4859-ba62-bacc07dd0020	31ff1ce9-f0a5-4b60-9557-4b0b14b34730
29248f0a-4203-4859-ba62-bacc07dd0020	1a0956b0-a0fd-49a6-8088-4f83abeb3b60
29248f0a-4203-4859-ba62-bacc07dd0020	9300886c-bdb0-4971-8544-81b33435aad7
29248f0a-4203-4859-ba62-bacc07dd0020	8e636ccc-a839-443f-b931-1f3f7af4f496
29248f0a-4203-4859-ba62-bacc07dd0020	466e82e0-93d4-4b33-b47d-47d2250108be
29248f0a-4203-4859-ba62-bacc07dd0020	9f728cd0-6030-4d4c-8ac6-9d8e56e4e772
29248f0a-4203-4859-ba62-bacc07dd0020	9283b594-5869-4303-a5b8-116eaea15a53
29248f0a-4203-4859-ba62-bacc07dd0020	ecbb91fe-e75b-4f8f-a3e5-44c3124aa7b9
29248f0a-4203-4859-ba62-bacc07dd0020	8567bb52-5658-422b-93fa-3f6efaa05b3a
29248f0a-4203-4859-ba62-bacc07dd0020	0713b69c-42d3-4ddc-a9b3-5a7aec6db0bd
29248f0a-4203-4859-ba62-bacc07dd0020	a4bf35ea-901a-40c3-bfed-d2f7e7acdc27
29248f0a-4203-4859-ba62-bacc07dd0020	d1543e47-c464-4b0f-80b5-65bb1df09dd6
29248f0a-4203-4859-ba62-bacc07dd0020	cb894db6-2be5-47fc-a23b-6c54a8e316f8
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	31ff1ce9-f0a5-4b60-9557-4b0b14b34730
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	13c22a6b-75ef-449f-a855-66219eb82b72
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	1a0956b0-a0fd-49a6-8088-4f83abeb3b60
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	9300886c-bdb0-4971-8544-81b33435aad7
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	8e636ccc-a839-443f-b931-1f3f7af4f496
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	466e82e0-93d4-4b33-b47d-47d2250108be
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	edda47ff-513e-4b53-b137-11e057c9066a
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	9283b594-5869-4303-a5b8-116eaea15a53
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	8567bb52-5658-422b-93fa-3f6efaa05b3a
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	0713b69c-42d3-4ddc-a9b3-5a7aec6db0bd
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	a4bf35ea-901a-40c3-bfed-d2f7e7acdc27
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	d1543e47-c464-4b0f-80b5-65bb1df09dd6
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	d44d89d9-cea1-4c1b-a2fd-0e4563ce4123
9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	951513c1-716d-44e9-a77d-fa5bb3f9db96
39bcb977-bc8b-438b-a05b-943ec6d2f79d	31ff1ce9-f0a5-4b60-9557-4b0b14b34730
39bcb977-bc8b-438b-a05b-943ec6d2f79d	13c22a6b-75ef-449f-a855-66219eb82b72
39bcb977-bc8b-438b-a05b-943ec6d2f79d	1a0956b0-a0fd-49a6-8088-4f83abeb3b60
39bcb977-bc8b-438b-a05b-943ec6d2f79d	9300886c-bdb0-4971-8544-81b33435aad7
39bcb977-bc8b-438b-a05b-943ec6d2f79d	8e636ccc-a839-443f-b931-1f3f7af4f496
39bcb977-bc8b-438b-a05b-943ec6d2f79d	466e82e0-93d4-4b33-b47d-47d2250108be
39bcb977-bc8b-438b-a05b-943ec6d2f79d	edda47ff-513e-4b53-b137-11e057c9066a
39bcb977-bc8b-438b-a05b-943ec6d2f79d	9283b594-5869-4303-a5b8-116eaea15a53
39bcb977-bc8b-438b-a05b-943ec6d2f79d	8567bb52-5658-422b-93fa-3f6efaa05b3a
39bcb977-bc8b-438b-a05b-943ec6d2f79d	0713b69c-42d3-4ddc-a9b3-5a7aec6db0bd
39bcb977-bc8b-438b-a05b-943ec6d2f79d	a4bf35ea-901a-40c3-bfed-d2f7e7acdc27
39bcb977-bc8b-438b-a05b-943ec6d2f79d	d1543e47-c464-4b0f-80b5-65bb1df09dd6
39bcb977-bc8b-438b-a05b-943ec6d2f79d	d44d89d9-cea1-4c1b-a2fd-0e4563ce4123
39bcb977-bc8b-438b-a05b-943ec6d2f79d	951513c1-716d-44e9-a77d-fa5bb3f9db96
\.


--
-- Data for Name: gymes; Type: TABLE DATA; Schema: public; Owner: radouane
--

COPY public.gymes (name, city_id, owner_id, location, description, price_by_month, price_by_year, profile_picture, links, id, created_at, updated_at) FROM stdin;
Neon X	c987eead-e7cc-4c83-80ac-6f5f525240d7	c34856af-322a-4b0b-a0f8-463c03b5194b	fake location t-123	This gym have a neon style	50	500	https://i.ibb.co/28gLW1q/neon-age.jpg	{}	bd24d3d1-a644-4106-9ece-3d09089f2269	2024-04-23 17:46:08.071839	2024-04-23 17:46:08.071912
The Champion	c77d94e6-9f82-4db1-8298-e69c64554cd4	5eb80932-e1fb-46cf-b1db-5ac618a41716	fake location S. near no where	A state-of-the-art gym equipped with the latest technology, offering personal training and a variety of classes to suit all fitness levels.	40	0	https://i.ibb.co/znFk4f8/champ.jpg	{}	2493a598-c8ce-470d-a03a-cea3ad8fcff7	2024-04-23 17:56:52.05771	2024-04-23 17:56:52.057781
Elite Fit Zone	c77d94e6-9f82-4db1-8298-e69c64554cd4	c34856af-322a-4b0b-a0f8-463c03b5194b	St. fake location	With a focus on holistic health, Elite Fit Zone provides yoga, Pilates, and meditation classes alongside traditional gym equipment.	60	599	https://i.ibb.co/JryJ0P5/elite-zone.jpg	{}	f5ee9697-646c-49ff-8153-3a48ac7ee865	2024-04-23 18:01:51.231403	2024-04-23 18:01:51.231463
Victory Gym	f5ecd4d2-fc08-47b2-b46d-046ab96421cb	c34856af-322a-4b0b-a0f8-463c03b5194b	New. Rabat	Focused on sports training and functional fitness, Victory Gym features obstacle courses and team-based workouts to keep things exciting.	20	0	https://i.ibb.co/Sr8xWH3/Victory-Gym.jpg	{}	45cf2b21-a1b1-4831-8e37-4dbc553d2d26	2024-04-23 18:36:10.311001	2024-04-23 18:36:10.311043
Core Balance Gym	1584bbaf-1207-4cff-94d9-ba6c0ca9d0c3	5eb80932-e1fb-46cf-b1db-5ac618a41716	St. fake location 234	Known for its balanced approach to fitness, this gym combines cardio, strength training, and flexibility exercises for a comprehensive workout.	40	0	https://i.ibb.co/6XjKbmy/Core-Balance-Gym.jpg	{}	bc53c1a8-b0af-4af0-9dc4-22f557f54d34	2024-04-23 18:42:20.146196	2024-04-23 18:42:20.146273
Powerhouse Athletic Club	f5ecd4d2-fc08-47b2-b46d-046ab96421cb	75fddd11-54d6-4db5-83b6-5c8e47fe2642	St. El Fateh	A popular spot for athletes and bodybuilders, offering a range of heavy-duty equipment and specialized training programs.	70	699	https://i.ibb.co/FJQH3C7/samuel-girven-fq-Mu99l8sqo-unsplash.jpg	{}	29248f0a-4203-4859-ba62-bacc07dd0020	2024-04-23 18:51:34.438793	2024-04-23 18:51:34.43883
FitNation Gym	c987eead-e7cc-4c83-80ac-6f5f525240d7	c34856af-322a-4b0b-a0f8-463c03b5194b	fake location 234	A high-end gym designed for athletes and serious fitness enthusiasts, with a variety of training zones and expert coaches to guide you.	100	1000	https://i.ibb.co/0tvLznY/Fit-Nation-Gym.jpg	{}	9b0d2a5f-74e7-455e-bfc9-2a38ddc29886	2024-04-23 18:57:05.869508	2024-04-23 18:57:05.869551
PowerFlex Gym	c987eead-e7cc-4c83-80ac-6f5f525240d7	5eb80932-e1fb-46cf-b1db-5ac618a41716	St. 264 fake location	A fun and energetic gym that focuses on versatility, offering cross-training, circuit workouts, and a fully-equipped weightlifting area.	80	700	https://i.ibb.co/x7GRk6R/Power-Flex-Gym.jpg	{}	39bcb977-bc8b-438b-a05b-943ec6d2f79d	2024-04-23 19:00:00.930041	2024-04-23 19:00:00.930099
\.


--
-- Data for Name: owners; Type: TABLE DATA; Schema: public; Owner: radouane
--

COPY public.owners (first_name, last_name, email, password, id, created_at, updated_at) FROM stdin;
Radouane	ABOUNOUAS	redouane@gmail.com	81dc9bdb52d04dc20036dbd8313ed055	c34856af-322a-4b0b-a0f8-463c03b5194b	2024-04-23 16:22:56.197537	2024-04-23 16:22:56.197587
John	WICK	john@gmail.com	81dc9bdb52d04dc20036dbd8313ed055	75fddd11-54d6-4db5-83b6-5c8e47fe2642	2024-04-23 16:23:27.4964	2024-04-23 16:23:27.496461
Halim	BOU	halim@gmail.com	81dc9bdb52d04dc20036dbd8313ed055	5eb80932-e1fb-46cf-b1db-5ac618a41716	2024-04-23 17:51:34.429714	2024-04-23 17:51:34.429799
\.


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: radouane
--

COPY public.reviews (gym_id, client_id, text, id, created_at, updated_at) FROM stdin;
\.


--
-- Name: amenities amenities_pkey; Type: CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.amenities
    ADD CONSTRAINT amenities_pkey PRIMARY KEY (id);


--
-- Name: cities cities_pkey; Type: CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.cities
    ADD CONSTRAINT cities_pkey PRIMARY KEY (id);


--
-- Name: clients clients_pkey; Type: CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_pkey PRIMARY KEY (id);


--
-- Name: gym_amenity gym_amenity_pkey; Type: CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.gym_amenity
    ADD CONSTRAINT gym_amenity_pkey PRIMARY KEY (gym_id, amenity_id);


--
-- Name: gymes gymes_pkey; Type: CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.gymes
    ADD CONSTRAINT gymes_pkey PRIMARY KEY (id);


--
-- Name: owners owners_pkey; Type: CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.owners
    ADD CONSTRAINT owners_pkey PRIMARY KEY (id);


--
-- Name: reviews reviews_pkey; Type: CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (id);


--
-- Name: gym_amenity gym_amenity_amenity_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.gym_amenity
    ADD CONSTRAINT gym_amenity_amenity_id_fkey FOREIGN KEY (amenity_id) REFERENCES public.amenities(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: gym_amenity gym_amenity_gym_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.gym_amenity
    ADD CONSTRAINT gym_amenity_gym_id_fkey FOREIGN KEY (gym_id) REFERENCES public.gymes(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: gymes gymes_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.gymes
    ADD CONSTRAINT gymes_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.cities(id);


--
-- Name: gymes gymes_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.gymes
    ADD CONSTRAINT gymes_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES public.owners(id);


--
-- Name: reviews reviews_client_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_client_id_fkey FOREIGN KEY (client_id) REFERENCES public.clients(id);


--
-- Name: reviews reviews_gym_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: radouane
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_gym_id_fkey FOREIGN KEY (gym_id) REFERENCES public.gymes(id);


--
-- PostgreSQL database dump complete
--

