<!-- 
Author: James Jeremiah
james2.jeremiah@uwe.ac.uk
Student number: 17042447

XSL to be placed within ITOnline's framework to read incoming emails sent to itonline.studentbot@uwe.ac.uk
-->

<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:msxsl="urn:schemas-microsoft-com:xslt">

<xsl:template match="/" name="Chatbot_XSL">
<BusinessObjectList SchemaVersion="1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="HierarchicalObjects-1.0.xsd">
		
		<!-- *********************** -->
		<!-- BEGIN: Define Variables -->
		<!-- *********************** -->
		
		<!-- find the profile link recid of the email sender -->
		<xsl:variable name="profilelink_recid">
		<!-- for each RelatedBusinessObject -->
		  <xsl:for-each select="BusinessObjectList/BusinessObject/RelatedBusinessObjectList/RelatedBusinessObject/BusinessObject">
			<xsl:choose>
			  <xsl:when test="@Name = 'Employee'">
				<xsl:for-each select="./FieldList/Field">
				  <xsl:choose>
					<xsl:when test="@Name = 'RecId'">
					  <xsl:value-of select="."/>
					</xsl:when>
				  </xsl:choose>
				</xsl:for-each>
			  </xsl:when>
			</xsl:choose>
		  </xsl:for-each>
		</xsl:variable>

		<!-- find the profile link category of the email sender -->
		<xsl:variable name="profilelink_cat">
		  <!-- for each RelatedBusinessObject -->
		  <xsl:for-each select="BusinessObjectList/BusinessObject/RelatedBusinessObjectList/RelatedBusinessObject/BusinessObject">
			<xsl:choose>
			  <xsl:when test="@Name = 'Employee'">
				<xsl:value-of select="'Employee'"/>
			  </xsl:when>
			</xsl:choose>
		  </xsl:for-each>
		</xsl:variable>
		
		<!-- find subject, subjectID, and user name-->
		<xsl:variable name="emailSubject" select = "BusinessObjectList/BusinessObject/EmailMessage/Subject" />
		<xsl:variable name="emailSubjectID" select = "BusinessObjectList/BusinessObject/EmailMessage/SubjectID" /> 
		<xsl:variable name="userName" select = "substring-before(BusinessObjectList/BusinessObject/EmailMessage/BodyHTML, ',')" /> 

		<!-- ********************* -->
		<!-- END: Define Variables -->
		<!-- ********************* -->
		<xsl:for-each select="BusinessObjectList/BusinessObject">	
			<xsl:element name="BusinessObject">
		<xsl:attribute name="Name"><xsl:text>ServiceReq</xsl:text></xsl:attribute>
		<!-- Set Transaction as 'Insert' -->
		<xsl:element name="Transaction">Insert</xsl:element>
		<!--Unique Key List-->
		<xsl:element name="UniqueKeyList">
			<xsl:element name="UniqueKey">
				<xsl:element name="Field">
					<xsl:attribute name="Name"><xsl:value-of select="'ServiceReqNumber'"/></xsl:attribute>
				</xsl:element>
			</xsl:element>
		</xsl:element>
				<FieldList>
					<!-- Fields -->
								<xsl:for-each select="EmailMessage/node()">
									<xsl:choose>
										<xsl:when test="name() = 'Subject'">
											<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:value-of select="'Subject'"/></xsl:attribute>
												<xsl:attribute name="Type">System.String</xsl:attribute>
												<xsl:value-of select="."/>
											</xsl:element>
										</xsl:when>
										<xsl:when test="name() = 'BodyHTML'">
											<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>Details</xsl:text></xsl:attribute>
												<xsl:attribute name="Type">System.String</xsl:attribute>
												<xsl:value-of select="."/>
											</xsl:element>
												<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>SvcReqTmplLink</xsl:text></xsl:attribute>
												<xsl:text>Request for Information</xsl:text>
											</xsl:element>
												<!-- xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>SvcReqTmplLink_RecID</xsl:text></xsl:attribute>
												<xsl:text>B96F31445446405D8EC2A312A6E55880</xsl:text >
											</xsl:element -->
												<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>SvcReqSubscLink_RecID</xsl:text></xsl:attribute>
												<xsl:text>396CC035BA064A6A980DB48C85293F1F</xsl:text> 
											</xsl:element>
											
											<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>Status</xsl:text></xsl:attribute>
												<xsl:choose>
													<xsl:when test="contains($emailSubject, 'RESOLVED')">
														<xsl:text>Request Complete</xsl:text>
													</xsl:when>
													<xsl:when test="contains($emailSubject, 'UNSOLVED')">
														<xsl:text>In Progress</xsl:text>
													</xsl:when>
													<xsl:otherwise>
														<xsl:text>Submitted</xsl:text>
													</xsl:otherwise>
												</xsl:choose>
											</xsl:element>
											
											<!--
											<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>Status</xsl:text></xsl:attribute>
												<xsl:text>Submitted</xsl:text>												
											</xsl:element>
											-->
											<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>Customer</xsl:text></xsl:attribute>
												<xsl:text>$userName</xsl:text>
											</xsl:element>
											
											<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>Source</xsl:text></xsl:attribute>
												<xsl:text>Email</xsl:text>
											</xsl:element>
											<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>OwnerTeam</xsl:text></xsl:attribute>
												<xsl:text>Service Desk</xsl:text>
											</xsl:element>
											<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>RecievedInboundEmail</xsl:text></xsl:attribute>
												<xsl:text>True</xsl:text>
											</xsl:element>
											
											<!--
											<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>ProfileLink_RecID</xsl:text></xsl:attribute>
												<xsl:value-of select="'FB884D18F7B746A0992880F2DFFE749C'"/>
											</xsl:element>
																							-->
											<!-- ... instead of mail senders RecId -->

								
											<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>ProfileLink_RecID</xsl:text></xsl:attribute>
												<xsl:value-of select="$profilelink_recid"/>
											</xsl:element>

											<xsl:element name="Field">
												<xsl:attribute name="Name"><xsl:text>ProfileLink_Category</xsl:text></xsl:attribute>
												<xsl:text>Employee</xsl:text>
											</xsl:element>

											
					<!--ProfileLink_Category>
				<xsl:element name="Field">
						<xsl:attribute name="Name"><xsl:text>ProfileLink_Category</xsl:text></xsl:attribute>
						<xsl:choose>
							<xsl:when test="string-length($profilelink_cat) > 0">
								<xsl:value-of select="$profilelink_cat"/>
							</xsl:when>
							<xsl:otherwise>
							
								<xsl:text>Employee</xsl:text>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:element>
				
					<xsl:element name="Field">
						<xsl:attribute name="Name"><xsl:text>ProfileLink_RecID</xsl:text></xsl:attribute>
						<xsl:choose>
							<xsl:when test="string-length($profilelink_recid) > 0">
								<xsl:value-of select="$profilelink_recid"/>
							</xsl:when>
							<xsl:otherwise>
					
								<xsl:text>FB884D18F7B746A0992880F2DFFE749C</xsl:text>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:element-->
										</xsl:when>
									</xsl:choose>
								</xsl:for-each>
							</FieldList>
							<!-- Copy the RelatedBusinessObjectList element-->
							<xsl:element name="RelatedBusinessObjectList">
								<xsl:for-each select="RelatedBusinessObjectList">
									<xsl:copy-of select="node()"/>
								</xsl:for-each>
							</xsl:element>
						</xsl:element>
					</xsl:for-each>	
		<!--</xsl:element> -->
	<!--</xsl:element> -->
		</BusinessObjectList>
		</xsl:template>
</xsl:stylesheet>